# MIT License
#
# Copyright (c) 2020 David Krasnitsky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

