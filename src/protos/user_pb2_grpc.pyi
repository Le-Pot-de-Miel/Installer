"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import grpc.aio
import typing
import user_pb2

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class UserStub:
    """The UserService defines the methods that our service exposes"""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    SignIn: grpc.UnaryUnaryMultiCallable[
        user_pb2.SignInSignUpRequest,
        user_pb2.UserResponse,
    ]
    SignUp: grpc.UnaryUnaryMultiCallable[
        user_pb2.SignInSignUpRequest,
        user_pb2.UserResponse,
    ]
    GetMe: grpc.UnaryUnaryMultiCallable[
        user_pb2.EmptyRequest,
        user_pb2.UserDto,
    ]
    ResetPassword: grpc.UnaryUnaryMultiCallable[
        user_pb2.PasswordRequest,
        user_pb2.EmptyResponse,
    ]
    ChangeEmail: grpc.UnaryUnaryMultiCallable[
        user_pb2.EmailRequest,
        user_pb2.EmptyResponse,
    ]
    InviteUser: grpc.UnaryUnaryMultiCallable[
        user_pb2.InviteUserRequest,
        user_pb2.UserDto,
    ]
    ActivateUser: grpc.UnaryUnaryMultiCallable[
        user_pb2.ActivateUserRequest,
        user_pb2.ActivateUserResponse,
    ]
    ChangeRights: grpc.UnaryUnaryMultiCallable[
        user_pb2.ChangeRightsRequest,
        user_pb2.UserDto,
    ]
    GetUsers: grpc.UnaryUnaryMultiCallable[
        user_pb2.EmptyRequest,
        user_pb2.GetUsersResponse,
    ]
    DeleteUser: grpc.UnaryUnaryMultiCallable[
        user_pb2.EmailRequest,
        user_pb2.EmptyResponse,
    ]
    ChangeLanguage: grpc.UnaryUnaryMultiCallable[
        user_pb2.ChangeLanguageRequest,
        user_pb2.EmptyResponse,
    ]
    GetUserLanguage: grpc.UnaryUnaryMultiCallable[
        user_pb2.UserRequest,
        user_pb2.UserLanguageResponse,
    ]
    GetHistory: grpc.UnaryUnaryMultiCallable[
        user_pb2.GetHistoryRequest,
        user_pb2.GetHistoryResponse,
    ]
    NightMode: grpc.UnaryUnaryMultiCallable[
        user_pb2.NightModeRequest,
        user_pb2.EmptyResponse,
    ]

class UserAsyncStub:
    """The UserService defines the methods that our service exposes"""

    SignIn: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.SignInSignUpRequest,
        user_pb2.UserResponse,
    ]
    SignUp: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.SignInSignUpRequest,
        user_pb2.UserResponse,
    ]
    GetMe: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.EmptyRequest,
        user_pb2.UserDto,
    ]
    ResetPassword: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.PasswordRequest,
        user_pb2.EmptyResponse,
    ]
    ChangeEmail: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.EmailRequest,
        user_pb2.EmptyResponse,
    ]
    InviteUser: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.InviteUserRequest,
        user_pb2.UserDto,
    ]
    ActivateUser: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.ActivateUserRequest,
        user_pb2.ActivateUserResponse,
    ]
    ChangeRights: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.ChangeRightsRequest,
        user_pb2.UserDto,
    ]
    GetUsers: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.EmptyRequest,
        user_pb2.GetUsersResponse,
    ]
    DeleteUser: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.EmailRequest,
        user_pb2.EmptyResponse,
    ]
    ChangeLanguage: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.ChangeLanguageRequest,
        user_pb2.EmptyResponse,
    ]
    GetUserLanguage: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.UserRequest,
        user_pb2.UserLanguageResponse,
    ]
    GetHistory: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.GetHistoryRequest,
        user_pb2.GetHistoryResponse,
    ]
    NightMode: grpc.aio.UnaryUnaryMultiCallable[
        user_pb2.NightModeRequest,
        user_pb2.EmptyResponse,
    ]

class UserServicer(metaclass=abc.ABCMeta):
    """The UserService defines the methods that our service exposes"""

    @abc.abstractmethod
    def SignIn(
        self,
        request: user_pb2.SignInSignUpRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.UserResponse, collections.abc.Awaitable[user_pb2.UserResponse]]: ...
    @abc.abstractmethod
    def SignUp(
        self,
        request: user_pb2.SignInSignUpRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.UserResponse, collections.abc.Awaitable[user_pb2.UserResponse]]: ...
    @abc.abstractmethod
    def GetMe(
        self,
        request: user_pb2.EmptyRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.UserDto, collections.abc.Awaitable[user_pb2.UserDto]]: ...
    @abc.abstractmethod
    def ResetPassword(
        self,
        request: user_pb2.PasswordRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.EmptyResponse, collections.abc.Awaitable[user_pb2.EmptyResponse]]: ...
    @abc.abstractmethod
    def ChangeEmail(
        self,
        request: user_pb2.EmailRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.EmptyResponse, collections.abc.Awaitable[user_pb2.EmptyResponse]]: ...
    @abc.abstractmethod
    def InviteUser(
        self,
        request: user_pb2.InviteUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.UserDto, collections.abc.Awaitable[user_pb2.UserDto]]: ...
    @abc.abstractmethod
    def ActivateUser(
        self,
        request: user_pb2.ActivateUserRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.ActivateUserResponse, collections.abc.Awaitable[user_pb2.ActivateUserResponse]]: ...
    @abc.abstractmethod
    def ChangeRights(
        self,
        request: user_pb2.ChangeRightsRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.UserDto, collections.abc.Awaitable[user_pb2.UserDto]]: ...
    @abc.abstractmethod
    def GetUsers(
        self,
        request: user_pb2.EmptyRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.GetUsersResponse, collections.abc.Awaitable[user_pb2.GetUsersResponse]]: ...
    @abc.abstractmethod
    def DeleteUser(
        self,
        request: user_pb2.EmailRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.EmptyResponse, collections.abc.Awaitable[user_pb2.EmptyResponse]]: ...
    @abc.abstractmethod
    def ChangeLanguage(
        self,
        request: user_pb2.ChangeLanguageRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.EmptyResponse, collections.abc.Awaitable[user_pb2.EmptyResponse]]: ...
    @abc.abstractmethod
    def GetUserLanguage(
        self,
        request: user_pb2.UserRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.UserLanguageResponse, collections.abc.Awaitable[user_pb2.UserLanguageResponse]]: ...
    @abc.abstractmethod
    def GetHistory(
        self,
        request: user_pb2.GetHistoryRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.GetHistoryResponse, collections.abc.Awaitable[user_pb2.GetHistoryResponse]]: ...
    @abc.abstractmethod
    def NightMode(
        self,
        request: user_pb2.NightModeRequest,
        context: _ServicerContext,
    ) -> typing.Union[user_pb2.EmptyResponse, collections.abc.Awaitable[user_pb2.EmptyResponse]]: ...

def add_UserServicer_to_server(servicer: UserServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
