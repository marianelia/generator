# import code_data_pb2
from enum import Enum 


class Access(Enum):
    PUBLIC = 1
    PROTECTED = 2
    PRIVATE = 3
    NONE = 4


class DataFromParam:
    def __init__(self, name ="", type="") -> None:
        self.set_name(name)
        self.set_type(type)

    def set_name(self, name:str) -> None:
        self.__name = name
    
    def set_type(self, type:str) -> None:
        self.__type = type

    def get_name(self) -> str:
        return self.__name
    
    def get_type(self) -> str:
        return self.__type

    name = property(get_name, set_name)
    type = property(get_type, set_type)

    def print_for_tests(self)-> None:
        print(self.name)
        print(self.type)

class DataFromVariable:
    def __init__(self, access: Access, param : DataFromParam) -> None:
        self.set_access(access)
        self.set_variable(param)

    def set_access(self, access: Access):
        self.__access = access

    def set_variable(self, param:DataFromParam):
        self.__variable = param

    def get_access(self) -> Access:
        return self.__access

    def get_variable(self) -> DataFromParam:
        return self.__variable
    
    access = property(get_access, set_access)
    param = property(get_variable, set_variable)

    def print_for_tests(self)-> None:
        print(self.__access)
        self.__variable.print_for_tests()

class DataFromFunc:
    def __init__(self, name="", output_param = "") -> None:
        self.__namespaces = []
        self.__name = name
        self.__output_param = output_param
        self.__list_input_params = []

    @property
    def namespaces(self) -> list:
        return self.__namespaces

    @namespaces.setter
    def namespaces(self, ns:str) -> None:
        self.__namespaces.append(ns)

    @namespaces.deleter
    def namespaces(self) -> None:
        self.__namespaces = []

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        self.__name = name

    @property
    def out_param(self) -> str:
        return self.__output_param

    @out_param.setter
    def out_param(self, out_param:str) -> None:
        self.__output_param = out_param

    @property
    def list_input_params(self) -> list:
        return self.__list_input_params
    
    @list_input_params.setter
    def list_input_params(self, inp_type:str, inp_name:str):
        self.add_inp_param(inp_type, inp_name)

    @list_input_params.deleter
    def list_input_params(self):
        self.__list_input_params = []

    def set_out_param_from_decl(self, out_param:str) -> None:
        self.__output_param = out_param.partition(' (')[0]

    def add_inp_param(self, inp_type:str, inp_name:str) -> None:
        input_params :DataFromParam = DataFromParam()
        input_params.type = inp_type
        input_params.name = inp_name
        self.__list_input_params.append(input_params)

    def get_inp_param_by_idx(self, index:int) -> DataFromParam:
        return self.__list_input_params[index]

    def print_for_tests(self) -> None:
        print(self.__namespaces)
        print(self.__name)
        print(self.__output_param)
        for num_inp_param in range(len(self.__list_input_params)):
            self.__list_input_params[num_inp_param].print_for_tests()


class DataFromMethod:
    def __init__(self, access, func) -> None:
        self.set_access(access)
        self.set_function(func)

    def set_access(self, access:Access) -> None:
        self.__access = access

    def set_function(self, func:DataFromFunc) -> None:
        self.__function = func

    def get_access(self) -> Access:
        return self.__access

    def get_function(self) -> DataFromFunc:
        return self.__function

    access = property(get_access, set_access)
    function = property(get_function, set_function)
        
    def print_for_tests(self)-> None:
        print(self.__access)
        self.__function.print_for_tests()



class DataFromStruct:
    def __init__(self, namespaces = [], name = "", 
                 default_access = Access.NONE, constructor = DataFromFunc()) -> None:
        self.__namespaces  = namespaces
        self.__name = name
        self.__default_access = default_access
        self.__list_methods :list[DataFromMethod] = []
        self.__list_variable :list[DataFromVariable] = []
        self.__constructor :DataFromFunc = constructor

    def __del__(self):
        del self.__namespaces
        del self.__name
        del self.__default_access
        del self.__list_methods
        del self.__list_variable

    @property 
    def constructor(self) -> DataFromFunc:
        return self.__constructor
    
    @constructor.setter
    def constructor(self, func:DataFromFunc):
        self.__constructor = func

    @property
    def access(self) -> Access:
        return self.__default_access
    
    @access.setter
    def access(self,access:Access) -> None:
        self.__default_access = access
    
    @property
    def namespaces(self) -> list:
        return self.__namespaces

    @namespaces.deleter
    def namespaces(self):
        self.__namespaces = []

    @namespaces.setter
    def namespaces(self, ns:str) -> None:
        self.__namespaces.append(ns)

    def set_namespace(self, ns:str) -> None:
        self.__namespaces.append(ns)

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        self.__name = name

    @property
    def methods(self) -> list:
        return self.__list_methods

    def set_method(self, access:str, func:DataFromFunc) -> None:
        method :DataFromMethod = DataFromMethod(access, func)
        self.__list_methods.append(method)

    def get_method_by_index(self, index:int) -> DataFromMethod:
        return self.__list_methods[index]

    def set_variable(self, access:str, var:DataFromParam) -> None:
        variable :DataFromVariable = DataFromVariable(access, var)
        self.__list_variable.append(variable)

    @property
    def variables(self) -> list:
        return self.__list_variable

    def get_variable_by_index(self, index:int) -> DataFromVariable:
        return self.__list_variable[index]

    def print_for_tests(self)-> None:
        print(self.__namespaces)
        print(self.__name)
        self.__constructor.print_for_tests()

        for num_method in range(len(self.__list_methods)):
            self.__list_methods[num_method].print_for_tests()

        for num_var in range(len(self.__list_variable)):
            self.__list_variable[num_var].print_for_tests()