from . import rskeyring

__doc__ = rskeyring.__doc__


def get_password(service: str, username: str) -> str:
    return rskeyring.get_password(service, username)


def set_password(service: str, username: str, password: str) -> None:
    return rskeyring.set_password(service, username, password)


def delete_password(service: str, username: str) -> None:
    return rskeyring.delete_password(service, username)

