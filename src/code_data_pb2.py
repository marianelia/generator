# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/code_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/code_data.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13src/code_data.proto\"\x1f\n\x07Project\x12\x14\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x05.File\"\\\n\x04\x46ile\x12\x14\n\x0cpath_to_file\x18\x01 \x01(\t\x12\x1c\n\x0bstruct_list\x18\x02 \x03(\x0b\x32\x07.Struct\x12 \n\rfunction_list\x18\x03 \x03(\x0b\x32\t.Function\"\x81\x01\n\x06Struct\x12\x11\n\tnamespace\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x07methods\x18\x03 \x03(\x0b\x32\x07.Method\x12\x1c\n\tvariables\x18\x04 \x03(\x0b\x32\t.Variable\x12\x1e\n\x0b\x63onstructor\x18\x05 \x01(\x0b\x32\t.Function\">\n\x06Method\x12\x17\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\x0e\x32\x07.Access\x12\x1b\n\x08\x66unction\x18\x02 \x01(\x0b\x32\t.Function\"_\n\x08\x46unction\x12\x11\n\tnamespace\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0coutput_param\x18\x03 \x01(\t\x12\x1c\n\x0cinput_params\x18\x04 \x03(\x0b\x32\x06.Param\"=\n\x08Variable\x12\x17\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\x0e\x32\x07.Access\x12\x18\n\x08variable\x18\x02 \x01(\x0b\x32\x06.Param\"#\n\x05Param\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t*:\n\x06\x41\x63\x63\x65ss\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02\x12\r\n\tPROTECTED\x10\x03\x62\x06proto3')
)

_ACCESS = _descriptor.EnumDescriptor(
  name='Access',
  full_name='Access',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLIC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECTED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=543,
  serialized_end=601,
)
_sym_db.RegisterEnumDescriptor(_ACCESS)

Access = enum_type_wrapper.EnumTypeWrapper(_ACCESS)
NONE = 0
PUBLIC = 1
PRIVATE = 2
PROTECTED = 3



_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='Project.files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=54,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path_to_file', full_name='File.path_to_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='struct_list', full_name='File.struct_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_list', full_name='File.function_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=148,
)


_STRUCT = _descriptor.Descriptor(
  name='Struct',
  full_name='Struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='Struct.namespace', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Struct.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methods', full_name='Struct.methods', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='Struct.variables', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constructor', full_name='Struct.constructor', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=280,
)


_METHOD = _descriptor.Descriptor(
  name='Method',
  full_name='Method',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access', full_name='Method.access', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function', full_name='Method.function', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=344,
)


_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='Function.namespace', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Function.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_param', full_name='Function.output_param', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_params', full_name='Function.input_params', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=441,
)


_VARIABLE = _descriptor.Descriptor(
  name='Variable',
  full_name='Variable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access', full_name='Variable.access', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variable', full_name='Variable.variable', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=504,
)


_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Param.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Param.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=541,
)

_PROJECT.fields_by_name['files'].message_type = _FILE
_FILE.fields_by_name['struct_list'].message_type = _STRUCT
_FILE.fields_by_name['function_list'].message_type = _FUNCTION
_STRUCT.fields_by_name['methods'].message_type = _METHOD
_STRUCT.fields_by_name['variables'].message_type = _VARIABLE
_STRUCT.fields_by_name['constructor'].message_type = _FUNCTION
_METHOD.fields_by_name['access'].enum_type = _ACCESS
_METHOD.fields_by_name['function'].message_type = _FUNCTION
_FUNCTION.fields_by_name['input_params'].message_type = _PARAM
_VARIABLE.fields_by_name['access'].enum_type = _ACCESS
_VARIABLE.fields_by_name['variable'].message_type = _PARAM
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Struct'] = _STRUCT
DESCRIPTOR.message_types_by_name['Method'] = _METHOD
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION
DESCRIPTOR.message_types_by_name['Variable'] = _VARIABLE
DESCRIPTOR.message_types_by_name['Param'] = _PARAM
DESCRIPTOR.enum_types_by_name['Access'] = _ACCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:Project)
  })
_sym_db.RegisterMessage(Project)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:File)
  })
_sym_db.RegisterMessage(File)

Struct = _reflection.GeneratedProtocolMessageType('Struct', (_message.Message,), {
  'DESCRIPTOR' : _STRUCT,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:Struct)
  })
_sym_db.RegisterMessage(Struct)

Method = _reflection.GeneratedProtocolMessageType('Method', (_message.Message,), {
  'DESCRIPTOR' : _METHOD,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:Method)
  })
_sym_db.RegisterMessage(Method)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTION,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:Function)
  })
_sym_db.RegisterMessage(Function)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLE,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:Variable)
  })
_sym_db.RegisterMessage(Variable)

Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
  'DESCRIPTOR' : _PARAM,
  '__module__' : 'src.code_data_pb2'
  # @@protoc_insertion_point(class_scope:Param)
  })
_sym_db.RegisterMessage(Param)


# @@protoc_insertion_point(module_scope)
