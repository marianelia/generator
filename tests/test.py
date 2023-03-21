import sys
import pathlib
sys.path.append(str(pathlib.Path(sys.path[0]).resolve().parent / "src"))

from data_deserialize import Data
from generating_cpp import *

root = str(pathlib.Path(sys.path[0]).resolve())

file_name = root + '/test'

if __name__ == '__main__':
    data_from_proto = Data()
    data_from_proto.deserialize_data(file_name)
    
    generate_file(data_from_proto, "main.cpp")
