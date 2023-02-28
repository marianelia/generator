from os import listdir
from os.path import isfile, join
from data_deserialize import *


path_to_datagen_headers = "datagen/include/datagen"
local_path_to_datagen_headers = "../" + path_to_datagen_headers


class GeneratingCode:
    def __init__(self) -> None:
        pass

    def gen_includes(self) -> str:
        
        generate_string_for_file:str = ""
        includes = self.datagen_files_to_includes()
        generate_string_for_file  = (generate_string_for_file + includes + "\n")

        #...
        return generate_string_for_file

    def generate_file(self, path_to_file:str):

        generating_includes = self.gen_includes()
        with open(path_to_file, mode='w', encoding="utf-8") as file:
            file.write(generating_includes)
            # file.write(....)

    def datagen_files_to_includes(self) -> str:
        list_files = [file_name for file_name in listdir(local_path_to_datagen_headers) 
                     if isfile(join(local_path_to_datagen_headers, file_name))]

        include_datagen:str = ""
        for file in list_files:
            include_datagen = (include_datagen + "\n" + 
                               "#include \"" + path_to_datagen_headers + "\\" + 
                               file + "\"")

        return include_datagen


