import sys
import pathlib
sys.path.append(str(pathlib.Path(sys.path[0]).resolve().parent / "src"))

from data_deserialize import Data
from generating_cpp import GeneratingCode

root = str(pathlib.Path(sys.path[0]).resolve())

file_name = root + '/test'

if __name__ == '__main__':
    print(file_name)
    data_from_proto = Data()
    data_from_proto.deserialize_data(file_name)

    gen_code = GeneratingCode()
    gen_code.gen_includes("main.cpp")
    # gen_code.datagen_files_to_includes()
