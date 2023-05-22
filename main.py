import sys
import pathlib
import os
import glob
sys.path.append(str(pathlib.Path(sys.path[0]).resolve() / "src"))

from data_deserialize import Data
from generating_cpp import *
from generating_cmakefile import *

# root = str(pathlib.Path(sys.path[0]).resolve())

# file_name = root + '/test'

# if __name__ == '__main__':
#     data_from_proto = Data()
#     data_from_proto.deserialize_data(file_name)

#     generate_file(data_from_proto, "main.cpp")
#     # generate_cmake("main.cpp") # and other settings

#     cmake_file = CMakeGen("project", "3.6", "17")
#     cmake_file.generate_cmake("..")



if __name__ == '__main__':
    if len(sys.argv) < 2: # позже переделать на 2 аргумента с -log?
        raise ValueError('The path to the library is not set')
    path_to_project = sys.argv[1]
    extension_dict = {}

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

    print(path_to_project)
    proto_files_list = glob.glob(path_to_project + '*_proto')
    print(proto_files_list)
    if len(proto_files_list) > 1:
        raise ValueError('Binary files with _proto more than one')
    proto_file_name = proto_files_list[0]


    data_from_proto = Data()
    data_from_proto.deserialize_data(proto_file_name)

    generate_file(data_from_proto, path_to_project + "main.cpp")
    #generate_cmake("main.cpp") # and other settings

    cmake_file = CMakeGen("project", path_to_project, "3.6", "17", library_name[0])
    cmake_file.generate_cmake_lists()