"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PutNewRulesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RULES_FIELD_NUMBER: builtins.int
    rules: builtins.str
    def __init__(
        self,
        *,
        rules: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["rules", b"rules"]) -> None: ...

global___PutNewRulesRequest = PutNewRulesRequest

@typing_extensions.final
class PutNewRulesReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PutNewRulesReply = PutNewRulesReply

@typing_extensions.final
class PutNewFiltersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILTERS_FIELD_NUMBER: builtins.int
    filters: builtins.str
    def __init__(
        self,
        *,
        filters: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filters", b"filters"]) -> None: ...

global___PutNewFiltersRequest = PutNewFiltersRequest

@typing_extensions.final
class PutNewFiltersReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PutNewFiltersReply = PutNewFiltersReply

@typing_extensions.final
class GetRulesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetRulesRequest = GetRulesRequest

@typing_extensions.final
class GetRulesReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RULES_FIELD_NUMBER: builtins.int
    FILTERS_FIELD_NUMBER: builtins.int
    rules: builtins.str
    filters: builtins.str
    def __init__(
        self,
        *,
        rules: builtins.str = ...,
        filters: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filters", b"filters", "rules", b"rules"]) -> None: ...

global___GetRulesReply = GetRulesReply
