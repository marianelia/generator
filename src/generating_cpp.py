from os import listdir
from os.path import isfile, join
from data_deserialize import *


path_to_datagen_headers = "datagen/include/datagen"
local_path_to_datagen_headers = "../project/" + path_to_datagen_headers


class GeneratingCode:
    def __init__(self, data:Data) -> None:
        self.__data_headers = data
        pass

    def generate_file(self, path_to_file:str):

        generating_includes = self.gen_includes()
        generating_main = self.gen_main()

        with open(path_to_file, mode='w', encoding="utf-8") as file:
            file.write(generating_includes)
            file.write(generating_main)
            # file.write(....)

    def gen_main(self) -> str:
        main_str = "int main() {"
        for data_func in range(len(self.__data_headers.get_list_func())):   #спрятать в get
            data_func.print_for_tests()

            for inp_param in data_func.get_inp_params():
                main_str += self.gen_inp_param_func(inp_param)
            
            main_str += self.gen_func(data_func)
            
        main_str +="}"

    def gen_func(self, func:DataFromFunc) -> str:
        gen_str:str = func.get_out_param() + " output_" + func.get_name() + " = "
        gen_str += self.gen_call_func(func)
        return gen_str

    def gen_call_func(self, func:DataFromFunc) -> str:
        gen_str = ""
        for ns in func.get_namespaces():
            gen_str += ns
            gen_str += "::"
        gen_str += func.get_name()
        gen_str += "("

        for inp_param in func.get_inp_params():
            gen_str += inp_param.type 
            gen_str += " "
            gen_str += inp_param.name

        gen_str += ");\n"
        return gen_str

    def gen_inp_param_func(self, inp_param : DataFromParam): #rename
        gen_str = inp_param.type + " " + inp_param.name + "="
        gen_str += "datagen::random<" + inp_param.type + ">();\n"
        return gen_str


    def gen_includes(self) -> str:
        generate_string_for_file:str = ""
        includes = self.datagen_files_to_includes()
        generate_string_for_file  = (generate_string_for_file + includes + "\n")

        #...
        return generate_string_for_file

    def datagen_files_to_includes(self) -> str:
        list_files = [file_name for file_name in listdir(local_path_to_datagen_headers) 
                     if isfile(join(local_path_to_datagen_headers, file_name))]

        include_datagen:str = ""
        for file in list_files:
            include_datagen = (include_datagen + "\n" + 
                               "#include \"" + path_to_datagen_headers + "\\" + 
                               file + "\"")

        return include_datagen


