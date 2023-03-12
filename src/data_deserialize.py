from classes_for_gen import *
import code_data_pb2

class Data:
    def __init__(self, list_data_func = [], list_data_struct = []) -> None:
        self.__list_data_func :list[DataFromFunc] = list_data_func
        self.__list_data_struct :list[DataFromStruct] = list_data_struct
        #...

    @property
    def list_func(self):
        return self.__list_data_func

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
        #print(file_obj.function_list)
        #print(file_obj.struct_list)
        for data_func in file_obj.function_list:
            self.add_data_from_func(self.deserialize_func(data_func))
        # for data_struct ....

    def deserialize_func(self, func_from_proto) -> DataFromFunc:
        func = DataFromFunc()
        for ns in func_from_proto.namespace:
            func.set_namespace(ns)
        
        func.name = func_from_proto.name
        func.output_param = func_from_proto.output_param
        
        for data_inp_param in func_from_proto.input_params:
            func.set_inp_params(data_inp_param.type, data_inp_param.name)
        func.print_for_tests()
        # self.__list_data_func.append(func)
        return func

    # def deserialize_input_params(self, param_from_proto) -> DataFromParam:
    #     return DataFromParam(param_from_proto.name, param_from_proto.type)
