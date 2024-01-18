"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import grpc.aio
import mobile_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class MobileStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetWireguardConfig: grpc.UnaryUnaryMultiCallable[
        mobile_pb2.WireguardConfigRequest,
        mobile_pb2.WireguardConfigResponse,
    ]

class MobileAsyncStub:
    GetWireguardConfig: grpc.aio.UnaryUnaryMultiCallable[
        mobile_pb2.WireguardConfigRequest,
        mobile_pb2.WireguardConfigResponse,
    ]

class MobileServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetWireguardConfig(
        self,
        request: mobile_pb2.WireguardConfigRequest,
        context: _ServicerContext,
    ) -> typing.Union[mobile_pb2.WireguardConfigResponse, collections.abc.Awaitable[mobile_pb2.WireguardConfigResponse]]: ...

def add_MobileServicer_to_server(servicer: MobileServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
