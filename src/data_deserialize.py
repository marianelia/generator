from data_units import *
import code_data_pb2

class Data:
    def __init__(self) -> None:
        self.__list_data_func :list[DataFromFunc] = []
        self.__list_data_struct :list[DataFromStruct] = []
        self.__files_name :list = [] 

    @property
    def files_name(self):
        return self.__files_name
    
    @files_name.setter
    def files_name(self, file_name:str):
        self.__files_name.append(file_name)

    @property
    def list_func(self):
        return self.__list_data_func
    
    @property
    def list_struct(self):
        return self.__list_data_struct

    def add_data_from_func(self, data:DataFromFunc) -> None:
        self.__list_data_func.append(data)
    
    def add_data_from_struct(self, data:DataFromStruct) -> None:
        self.__list_data_struct.append(data)


    def deserialize_data_from_file(self, file_name:str) -> bytes:
        with open(file_name, 'rb') as file:
            serialize_to_string = file.read()
        return serialize_to_string

    def deserialize_data(self, path_to_output_file:str):
        serialize_to_string = self.deserialize_data_from_file(path_to_output_file)

        project_obj = code_data_pb2.Project()
        project_obj.ParseFromString(serialize_to_string)

        for file_obj in project_obj.files:
            self.files_name = file_obj.path_to_file
            for data_func in file_obj.function_list:
                self.add_data_from_func(self.deserialize_func(data_func))

            for data_struct in file_obj.struct_list:
                self.add_data_from_struct(self.deserialize_struct(data_struct))

    def deserialize_func(self, func_from_proto) -> DataFromFunc:
        func = DataFromFunc()
        del func.namespaces
        for ns in func_from_proto.namespace:
            func.namespaces = ns
        
        func.name = func_from_proto.name
        func.out_param = func_from_proto.output_param
        
        for data_inp_param in func_from_proto.input_params:
            func.add_inp_param(data_inp_param.type, data_inp_param.name)
        # func.print_for_tests()
        return func
    
    def deserialize_struct(self, struct_from_proto) -> DataFromStruct:
        struct = DataFromStruct()
        del struct.namespaces
        for ns in struct_from_proto.namespace:
            struct.namespaces = ns

        struct.name = struct_from_proto.name
        struct.constructor = self.deserialize_func(struct_from_proto.constructor)

        for method_proto in struct_from_proto.methods:
            data_func = method_proto.function
            struct.set_method(method_proto.access, self.deserialize_func(data_func))

        for var_proto in struct_from_proto.variables:
            param_proto = var_proto.variable
            data_param = DataFromParam(param_proto.name, param_proto.type)
            struct.set_variable(var_proto.access, data_param)

        # struct.print_for_tests()
        return struct




