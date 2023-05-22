'''
CMakeList.txt для тестов: создание внутреннего и ht с Datagen
'''
import sys
import pathlib
import os

CMAKE_LIST_TXT = "CMakeLists.txt"

# path_to_datagen_headers = "datagen/include/datagen"
# local_path_to_datagen_headers = "../project/" + path_to_datagen_headers
path_to_boost = "/usr/lib/x86_64-linux-gnu/cmake/Boost-1.71.0"



class CMakeGen:
    def __init__(self, project_name:str, path_to_file:str,
                  cmake_version:str, cxx_standard:str, library_name:str) -> None:
        self.__project_name = project_name
        self.__cmake_version = cmake_version
        self.__cxx_standard = cxx_standard
        self.__path_to_file = path_to_file
        self.__library_name = library_name
        #путь к глобальному CMakeLisxt

    @property
    def project_name(self):
        return self.__project_name
    
    @property
    def cmake_version(self):
        return self.__cmake_version
    
    @property
    def cxx_standard(self):
        return self.__cxx_standard
    
    @property
    def path_to_file(self):
        return self.__path_to_file
    
    @property
    def library_name(self):
        return self.__library_name
    
    

    def generate_cmake_lists(self):
        self.generate_local_cmake()
        self.change_path_in_global_cmake_list()


    def generate_local_cmake(self): 
        cmake_file = ""
        cmake_file += self.__add_cmake_version()
        cmake_file += self.__add_set("CMAKE_CXX_STANDARD", self.cxx_standard)
        cmake_file += self.__add_project_name()
        cmake_file += self.__add_set("SOURCE_FILES", "main.cpp")
        cmake_file += self.__add_executable()
        cmake_file += "option(BUILD_SHARED_LIBS \"Build using shared libraries\" ON)\n"
        cmake_file += self.__target_include_dir_for_datagen()
        cmake_file += self.__add_imported_library(self.library_name, "SHARED")


        cmake_file += self.__add_defined_boost()

        path_to_file_with_cmake_list = self.path_to_file
        if path_to_file_with_cmake_list[-1] != '/':
            path_to_file_with_cmake_list += '/'
        path_to_file_with_cmake_list += CMAKE_LIST_TXT # учитывать слэш
        with open(path_to_file_with_cmake_list, mode='w', encoding="utf-8") as file:
            file.write(cmake_file)

    def generate_global_cmake_file(self): #костыльно,но тут неизменяемые строки
        cmake_file = ""
        cmake_file += self.__add_cmake_version()
        cmake_file += "project(datagen_lib)\n"
        cmake_file += self.__add_set("BOOST_ROOT", path_to_boost)
        cmake_file += "find_package(Boost REQUIRED COMPONENTS system filesystem random)\n"
        cmake_file += "set(CMAKE_CXX_FLAGS \"${CMAKE_CXX_FLAGS} -DBOOST_ALL_NO_LIB -DBOOST_LOG_DYN_LINK\")\n"
        cmake_file += self.__add_subdirectory("datagen")
        cmake_file += self.__add_subdirectory(self.path_to_file, True)
        return cmake_file

    def __add_subdirectory(self, subdir:str, use_dir_build:bool = False):
        path_to_subdir = subdir

        if path_to_subdir[-1] == '/':
            path_to_subdir = path_to_subdir[:-1]   
        subdir_str = "add_subdirectory(" + path_to_subdir
        if use_dir_build == True:
            subdir_str += " ${CMAKE_CURRENT_BINARY_DIR}/project_build"
        subdir_str += ")\n"
        return subdir_str
    
    def __add_defined_boost(self):
        def_str = "if (DEFINED Boost_INCLUDE_DIR)\n"
        def_str += "\ttarget_link_libraries(" + self.project_name + " ${Boost_LIBRARIES})\n"
        def_str += "endif ()"
        return def_str
    
    def __target_include_dir_for_datagen(self):
        return ("target_include_directories(" + self.project_name + 
                " PRIVATE ${datagen_SOURCE_DIR}/include)\n")

    def change_path_in_global_cmake_list(self):
        path_to_cmakelist_global = str(pathlib.Path(sys.path[0]).resolve().parent) 
        if path_to_cmakelist_global[-1] != '/':
            path_to_cmakelist_global += '/'
        path_to_cmake_file = path_to_cmakelist_global + CMAKE_LIST_TXT
        print(path_to_cmake_file)
        global_cmake_list = self.generate_global_cmake_file()
        with open(path_to_cmake_file, mode='w', encoding="utf-8") as file:
            file.write(global_cmake_list)

    def __add_cmake_version(self) -> str:
        return "cmake_minimum_required(VERSION " + self.cmake_version + ")\n"

    def __add_project_name(self) -> str:
        return "project(" + self.__project_name + ")\n"

    def __add_set(self, var:str, meaning:str) -> str:
        return "set(" + var + " " + meaning + ")\n"

    def __add_imported_library(self, lib:str, type:str) -> str:
        name_lib = lib[:-3]
        print(name_lib[:3])
        if name_lib[:3] == "lib":
            name_lib = name_lib[3:]
        print(name_lib)
        import_lib = "add_library(" + name_lib + " " + type + " IMPORTED)\n"
        import_lib = (import_lib + "target_link_libraries(" + self.project_name +
                      " ${PROJECT_SOURCE_DIR}/" + lib + ")\n")
        return import_lib

    # def __find_lib(self) -> str:
    #     for root, dirs, files in os.walk(path_to_project):
    #         for name in files:
    #             if(name.endswith(".so")):
    #                 print
    #                 return name
                
        #exeption

    def __add_executable(self) -> str:
        return "add_executable(" + self.__project_name + " ${SOURCE_FILES})\n"


# path_to_datagen_headers = "datagen/include/datagen"
# local_path_to_datagen_headers = "../project/" + path_to_datagen_headers
# path_to_boost = "/usr/lib/x86_64-linux-gnu/cmake/Boost-1.71.0"
# path_to_project = str(pathlib.Path(sys.path[0]).resolve().parent) #временный


# class CMakeGen:
#     def __init__(self, project_name:str, cmake_version:str, cxx_standard:str) -> None:
#         self.__project_name = project_name
#         self.__cmake_version = cmake_version
#         self.__cxx_standard = cxx_standard

#     @property
#     def project_name(self):
#         return self.__project_name
    
#     @property
#     def cmake_version(self):
#         return self.__cmake_version
    
#     @property
#     def cxx_standard(self):
#         return self.__cxx_standard

#     def generate_cmake(self, path_to_file:str) -> str:
#         cmake_file = ""
#         cmake_file += self.__add_cmake_version()
#         cmake_file += self.__add_project_name()
#         cmake_file += self.__add_set("CMAKE_CXX_STANDARD", self.cxx_standard)
#         cmake_file += self.__add_set("SOURCE_FILES", "main.cpp")
#         cmake_file += self.__add_imported_library("input_lib", "SHARED")
#         cmake_file += self.__add_executable()
#         cmake_file += self.__add_datagen_lib()

#         path_to_file += "/CMakeLists.txt" # учитывать слэш
#         with open(path_to_file, mode='w', encoding="utf-8") as file:
#             file.write(cmake_file)

#     def __add_cmake_version(self) -> str:
#         return "cmake_minimum_required(VERSION " + self.__cmake_version + ")\n"

#     def __add_project_name(self) -> str:
#         return "project(" + self.__project_name + ")\n"

#     def __add_set(self, var:str, meaning:str) -> str:
#         return "set(" + var + " " + meaning + ")\n"

#     def __add_imported_library(self, name_lib:str, type:str) -> str:
#         import_lib = "add_library(" + name_lib + " " + type + " IMPORTED)\n"
#         import_lib = (import_lib + "set_property(TARGET " + name_lib + 
#                         " PROPERTY IMPORTED_LOCATION " + self.__find_lib() + ")\n")
#         import_lib = import_lib + "target_link_libraries(${TARGET} input_lib)\n"
#         return import_lib

#     def __find_lib(self) -> str:
#         for root, dirs, files in os.walk(path_to_project):
#             for name in files:
#                 if(name.endswith(".so")):
#                     print
#                     return name
                
#         #exeption

#     def __add_executable(self) -> str:
#         return "add_executable(" + self.__project_name + " ${SOURCE_FILES})\n"

#     def __add_datagen_lib(self) -> str:
#         return "target_include_directories(" + self.__project_name + " PRIVATE ${datagen_SOURCE_DIR}/include)\n" 



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

