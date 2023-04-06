import sys
import pathlib
sys.path.append(str(pathlib.Path(sys.path[0]).resolve().parent / "src"))

from data_deserialize import Data
from generating_cpp import *
from generating_cmakefile import *

root = str(pathlib.Path(sys.path[0]).resolve())

file_name = root + '/test'

if __name__ == '__main__':
    data_from_proto = Data()
    data_from_proto.deserialize_data(file_name)

    generate_file(data_from_proto, "main.cpp")
    # generate_cmake("main.cpp") # and other settings

    cmake_file = CMakeGen("project", "3.6", "17")
    cmake_file.generate_cmake("..")


    
