'''
CMakeList.txt для тестов (внутренний)
'''
import sys
import pathlib
import os

path_to_datagen_headers = "datagen/include/datagen"
local_path_to_datagen_headers = "../project/" + path_to_datagen_headers
path_to_boost = "/usr/lib/x86_64-linux-gnu/cmake/Boost-1.71.0"
path_to_project = str(pathlib.Path(sys.path[0]).resolve())


class CMakeGen:
    def __init__(self, project_name:str, cmake_version:str, cxx_standard:str) -> None:
        self.__project_name = project_name
        self.__cmake_version = cmake_version
        self.__cxx_standard = cxx_standard

    @property
    def project_name(self):
        return self.__project_name
    
    @property
    def cmake_version(self):
        return self.__cmake_version
    
    @property
    def cxx_standard(self):
        return self.__cxx_standard

    def generate_cmake(self, path_to_file:str) -> str:
        cmake_file = ""
        cmake_file += self.__add_cmake_version()
        cmake_file += self.__add_project_name()
        cmake_file += self.__add_set("CMAKE_CXX_STANDARD", self.cxx_standard)
        cmake_file += self.__add_set("SOURCE_FILES", "main.cpp")
        cmake_file += self.__add_imported_library("input_lib", "SHARED")
        cmake_file += self.__add_executable()
        cmake_file += self.__add_datagen_lib()


        with open(path_to_file, mode='w', encoding="utf-8") as file:
            file.write()

    def __add_cmake_version(self) -> str:
        return "cmake_minimum_required(VERSION " + self.__cmake_version + ")\n"

    def __add_project_name(self) -> str:
        return "project(" + self.__project_name + ")\n"

    def __add_set(self, var:str, meaning:str) -> str:
        return "set(" + var + " " + meaning + ")\n"

    def __add_imported_library(self, name_lib:str, type:str) -> str:
        import_lib = "add_library(" + name_lib + " " + type + " IMPORTED)\n"
        import_lib = (import_lib + "set_property(TARGET " + name_lib + 
                        " PROPERTY IMPORTED_LOCATION " + self.__find_lib() + ")\n")
        import_lib = import_lib + "target_link_libraries(${TARGET} input_lib)\n"
        return import_lib

    def __find_lib(self) -> str:
        for root, dirs, files in os.walk(path_to_project):
            for name in files:
                if(name.endswith(".so")):
                    return name
                
        #exeption

    def __add_executable(self) -> str:
        return "add_executable(" + self.__project_name + " ${SOURCE_FILES})"

    def __add_datagen_lib(self) -> str:
        return "target_include_directories(" + self.__project_name + " PRIVATE ${datagen_SOURCE_DIR}/include)" 



# def generate_cmake(path_to_sourse:str):
#     pass

# def add_cmake_version(version:str) -> str:
#     return "cmake_minimum_required(VERSION " + version + ")"

# def add_cxx_standart(std:str) -> str:
#     return "set(CMAKE_CXX_STANDARD " + std + ")"

# def add_project_name(name:str) -> str:
#     return "project(" + name + ")"

# def add_source_files(files:list)->str:
#     source_files = ""


# def add_cmake_flags() -> str: #в дальнейшем флаги передавать
#     pass

# def add_boost_root(path_to_boost:str) -> str:
#     pass

# def add_find_package() -> str:
#     pass

