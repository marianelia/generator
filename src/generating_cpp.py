from os import listdir
from os.path import isfile, join
from data_deserialize import *


path_to_datagen_headers = "datagen/include/datagen"
local_path_to_datagen_headers = "../project/" + path_to_datagen_headers

def generate_file(data:Data, path_to_file:str):
    generating_includes = gen_includes(data.files_name)
    generating_main = gen_main(data)

    with open(path_to_file, mode='w', encoding="utf-8") as file:
        file.write(generating_includes)
        file.write(generating_main)
        # file.write(....)

def gen_main(data:Data) -> str:
    main_str = "int main() {\n"

    for data_func in data.list_func:   #спрятать в get
        for inp_param in data_func.list_input_params:
            main_str += gen_inp_param_func(inp_param)
        
        main_str += gen_func(data_func)
            
    main_str +="\n}"
    return main_str

def gen_func(func:DataFromFunc) -> str:
    gen_str = ""
    gen_str = func.out_param + " output_" + func.name + " = "
    gen_str += gen_call_func(func)
    return gen_str

def gen_call_func(func:DataFromFunc) -> str:
    gen_str = ""
    for ns in func.namespaces:
        gen_str += ns
        gen_str += "::"
    gen_str += func.name
    gen_str += "("

    # del func.namespaces
    if (len(func.list_input_params) > 0):
        for inp_param in func.list_input_params:
            gen_str += inp_param.name
            gen_str += ","
        gen_str = gen_str[:-1]

    # del func.list_input_params
    gen_str += ");\n"
    return gen_str

def gen_inp_param_func(inp_param : DataFromParam): #rename
    gen_str = inp_param.type + " " + inp_param.name + "="
    gen_str += "datagen::random<" + inp_param.type + ">();\n"
    return gen_str


def gen_includes(files_name) -> str:
    generate_string_for_file:str = ""
    includes = datagen_files_to_includes()
    includes_local = gen_includes_local_files(files_name)
    generate_string_for_file  = (generate_string_for_file + includes + 
                                 includes_local +"\n")


    #...
    return generate_string_for_file

def gen_includes_local_files(files_name) -> str:
    include_for_project = ""

    include_for_project = (include_for_project + "\n" + 
                           "#include <" + 
                           files_name + ">")


    return include_for_project

def datagen_files_to_includes() -> str:
    list_files = [file_name for file_name in listdir(local_path_to_datagen_headers) 
                     if isfile(join(local_path_to_datagen_headers, file_name))]

    include_datagen:str = ""
    for file in list_files:
        include_datagen = (include_datagen + "\n" + 
                           "#include <datagen/" + 
                           file + ">")

    return include_datagen