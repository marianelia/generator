from classes_for_gen import *
import code_data_pb2

class Data:
    def __init__(self) -> None:
        self.__list_data_func :list[DataFromFunc] = []
        self.__list_data_struct :list[DataFromStruct] = []
        #...

    def add_data_from_func(self, data:DataFromFunc) -> None:
        self.__list_data_func.append(data)
    
    def add_data_from_struct(self, data:DataFromStruct) -> None:
        self.__list_data_struct.append(data)


    def deserialize_data_to_file(self, file_name:str) -> bytes:
        with open(file_name, 'rb') as file:
            serialize_to_string = file.read()
        return serialize_to_string

    def deserialize_data(self, path_to_output_file:str):
        serialize_to_string = self.deserialize_data_to_file(path_to_output_file)

        file_obj = code_data_pb2.File()
        file_obj.ParseFromString(serialize_to_string)
        print(file_obj.function_list)
        print(file_obj.struct_list)
        # for data_func in file_obj.function_list:
            # self.add_data_from_func(data_func)
        # for data_struct ....

