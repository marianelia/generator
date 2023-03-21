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

    for data_func in data.list_func:
        main_str += gen_func_data(data_func)

    for data_struct in data.list_struct:
        main_str += gen_struct_data(data_struct)

    main_str +="\n}"
    return main_str

def gen_struct_data(data_struct:DataFromStruct)-> str:
    struct_str =""
    ptr_name = gen_name_ptr_to_struct(data_struct)
    struct_str += gen_ptr_new_struct(data_struct, ptr_name)
    for method in data_struct.methods:
        struct_str += gen_method(method, ptr_name)

    #get variable - gen_inp_param_func

    return struct_str

def gen_method(data_method:DataFromMethod, ptr_name:str) -> str:
    methods_str = ""
    if data_method.access == 1:     #TODO понять,почему не получается применить Access.PUBLIC
        methods_str += gen_func_data(data_method.function, ptr_name)
    return methods_str

def gen_ptr_new_struct(data_struct:DataFromStruct, ptr_name:str) ->str:
    struct_ptr = ""

    for inp_param in data_struct.constructor.list_input_params:
        struct_ptr += gen_inp_param_func(inp_param)

    struct_ptr = (struct_ptr + gen_namespaces(data_struct.namespaces) + 
                  data_struct.name + "* " + ptr_name + " = new ")
    if data_struct.constructor.name == '':
        struct_ptr = (struct_ptr + gen_namespaces(data_struct.namespaces) + 
                      data_struct.name + "();")
        return struct_ptr

    struct_ptr += gen_call_constructor(data_struct)
    return struct_ptr

def gen_call_constructor(data_struct:DataFromStruct) -> str:
    constr_str = ""
    constr_str += gen_namespaces(data_struct.namespaces)
    constr_str += data_struct.constructor.name
    constr_str += "("
    constr_str += gen_str_for_call_from_input_param(data_struct.constructor.list_input_params)
    constr_str += ");\n"

    return constr_str

def gen_name_ptr_to_struct(data_struct:DataFromStruct) -> str:
    return "ptr_" + data_struct.name

def gen_func_data(data_func:DataFromFunc, ptr_name_for_methods="") -> str:
    func_str = ""
    for inp_param in data_func.list_input_params:
        func_str += gen_inp_param_func(inp_param)
        
    func_str += gen_func_call(data_func, ptr_name_for_methods)
    return func_str

def gen_inp_param_func(inp_param : DataFromParam): #rename
    gen_str = inp_param.type + " " + inp_param.name + "="
    gen_str += "datagen::random<" + inp_param.type + ">();\n"
    return gen_str

def gen_func_call(func:DataFromFunc, ptr_name_for_methods="") -> str:
    gen_str = ""
    if func.out_param != "void":
        gen_str = func.out_param + " output_" + func.name + " = "
    gen_str += gen_name_func(func, ptr_name_for_methods)
    return gen_str

def gen_namespaces(ns_list) -> str:
    gen_str = ""
    for ns in ns_list:
        gen_str += ns
        gen_str += "::"
    return gen_str

def gen_name_func(func:DataFromFunc, ptr_name_for_methods="") -> str:
    gen_str = ""
    gen_str += gen_namespaces(func.namespaces)
    if ptr_name_for_methods != "":
        gen_str += ptr_name_for_methods 
        gen_str += "->"
    gen_str += func.name
    gen_str += "("
    gen_str += gen_str_for_call_from_input_param(func.list_input_params)

    # del func.list_input_params
    gen_str += ");\n"
    return gen_str

def gen_str_for_call_from_input_param(list_inp_params:DataFromParam) -> str:
    gen_str = ""
    if (len(list_inp_params) > 0):
        for inp_param in list_inp_params:
            gen_str += inp_param.name
            gen_str += ","
        gen_str = gen_str[:-1]
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