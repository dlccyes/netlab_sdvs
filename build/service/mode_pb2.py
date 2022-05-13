# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mode.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmode.proto\"\x1b\n\x0bModeRequest\x12\x0c\n\x04mode\x18\x01 \x01(\t\"\x1e\n\x0cModeResponse\x12\x0e\n\x06result\x18\x01 \x01(\t25\n\x0bModeChanger\x12&\n\x07\x43ompute\x12\x0c.ModeRequest\x1a\r.ModeResponseb\x06proto3'
)




_MODEREQUEST = _descriptor.Descriptor(
  name='ModeRequest',
  full_name='ModeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='ModeRequest.mode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=14,
  serialized_end=41,
)


_MODERESPONSE = _descriptor.Descriptor(
  name='ModeResponse',
  full_name='ModeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ModeResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=43,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['ModeRequest'] = _MODEREQUEST
DESCRIPTOR.message_types_by_name['ModeResponse'] = _MODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModeRequest = _reflection.GeneratedProtocolMessageType('ModeRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODEREQUEST,
  '__module__' : 'mode_pb2'
  # @@protoc_insertion_point(class_scope:ModeRequest)
  })
_sym_db.RegisterMessage(ModeRequest)

ModeResponse = _reflection.GeneratedProtocolMessageType('ModeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODERESPONSE,
  '__module__' : 'mode_pb2'
  # @@protoc_insertion_point(class_scope:ModeResponse)
  })
_sym_db.RegisterMessage(ModeResponse)



_MODECHANGER = _descriptor.ServiceDescriptor(
  name='ModeChanger',
  full_name='ModeChanger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=75,
  serialized_end=128,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='ModeChanger.Compute',
    index=0,
    containing_service=None,
    input_type=_MODEREQUEST,
    output_type=_MODERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODECHANGER)

DESCRIPTOR.services_by_name['ModeChanger'] = _MODECHANGER

# @@protoc_insertion_point(module_scope)