import sys
import pathlib
import os
import glob
from enum import Enum
sys.path.append(str(pathlib.Path(sys.path[0]).resolve() / "src"))

from data_deserialize import Data
from generating_cpp import *
from generating_cmakefile import *

if __name__ == '__main__':
    class Mode(Enum):
        NONE = 1
        TEST = 2

    mode = Mode.NONE
    extension_dict = {}
    cpp_file_name = 'main.cpp'
    project_name = 'project'


    if len(sys.argv) < 2:
        raise ValueError('The path to the library is not set')
    if len(sys.argv) > 3:
        raise ValueError('The arguments are incorrectly set')

    if len(sys.argv) == 3:
        if sys.argv[1] != '-test':
            raise ValueError('The option is incorrectly set')
        path_to_project = sys.argv[2]
        mode = Mode.TEST

    if len(sys.argv) == 2:
        path_to_project = sys.argv[1]
 
    for root, _, files in os.walk(path_to_project):
        for name in files:
            extension = os.path.splitext(name)[1]
            if extension in extension_dict:
                extension_dict[extension].append(name)
            else:
                extension_dict[extension] = [name]
        library_name = extension_dict.get('.so', [])
        if len(library_name) == 0:
            raise FileNotFoundError('There are no libraries with the *.so extension in the directory')
        elif len(library_name) > 1:
            raise ValueError('Libraries with an extension *.so more than one')

     
    if path_to_project[-1] != '/':
        path_to_project += '/'

    proto_files_list = glob.glob(path_to_project + '*_proto')
    if len(proto_files_list) > 1:
        raise ValueError('Binary files with _proto more than one')
    if len(proto_files_list) < 1:
        raise ValueError('Binary file with _proto not find')
    proto_file_name = proto_files_list[0]


    data_from_proto = Data()
    data_from_proto.deserialize_data(proto_file_name)

    if mode == Mode.NONE:
        generate_file(data_from_proto, path_to_project + cpp_file_name)
        #generate_cmake("main.cpp") # and other settings
        cmake_file = CMakeGen(project_name, path_to_project, "3.6", "17", library_name[0])
        cmake_file.generate_cmake_lists()

    elif mode == Mode.TEST:
        generate_file_with_tests(data_from_proto, path_to_project + cpp_file_name, cpp_file_name)