from . import rskeyring

__doc__ = rskeyring.__doc__


def get_password(service: str, username: str) -> str:
    """
    A function to get a stored password (secret item) from a specified service name & username (key).

    Raises "OSError" exception if item does not exists or otherwise cannot be retrieved.

    :param service: A unique service name
    :param username: A key name
    :return: Password (secret item)
    """
    return rskeyring.get_password(service, username)


def set_password(service: str, username: str, password: str) -> None:
    """
    A function that stores or updates a password (secret item) by a specified service name & username (key).

    Raises "OSError" exception if unable to set or update the password (secret item).

    :param service: A unique service name
    :param username: A key name
    :param password: A secret item
    :return: None
    """
    return rskeyring.set_password(service, username, password)


def delete_password(service: str, username: str) -> None:
    """
    A function to delete a stored password (secret item), specified by a service name & username (key).

    Raises "OSError" exception if item does not exists or otherwise unable to comply.

    :param service: A unique service name
    :param username: A key name
    :return: None
    """
    return rskeyring.delete_password(service, username)

