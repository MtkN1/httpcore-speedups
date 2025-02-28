import contextlib
import typing

ExceptionMapping = typing.Mapping[typing.Type[Exception], typing.Type[Exception]]


@contextlib.contextmanager
def map_exceptions(map: ExceptionMapping) -> typing.Iterator[None]:
    try:
        yield
    except Exception as exc:  # noqa: PIE786
        for from_exc, to_exc in map.items():
            if isinstance(exc, from_exc):
                raise to_exc(exc) from exc
        raise  # pragma: nocover


class ConnectionNotAvailable(Exception):
    """
    This error is handled by the connection pool.
    Users should not see this error directly when using connection pool.
    """


class ServerDisconnectedError(ConnectionNotAvailable):
    """
    This error is handled by the connection pool.
    Users should not see this error directly when using connection pool.
    """


class ProxyError(Exception):
    pass


class UnsupportedProtocol(Exception):
    pass


class ProtocolError(Exception):
    pass


class RemoteProtocolError(ProtocolError):
    pass


class LocalProtocolError(ProtocolError):
    pass


# Timeout errors


class TimeoutException(Exception):
    pass


class PoolTimeout(TimeoutException):
    pass


class ConnectTimeout(TimeoutException):
    pass


class ReadTimeout(TimeoutException):
    pass


class WriteTimeout(TimeoutException):
    pass


# Network errors


class NetworkError(Exception):
    pass


class ConnectError(NetworkError):
    pass


class ReadError(NetworkError):
    pass


class WriteError(NetworkError):
    pass
