# rskeyring (Rust Keyring)
A C-level keyring bind from Rust's crate created by hwchen (https://github.com/hwchen/keyring-rs).

# Motivation
Since using _pypi.org_ keyring library to store sensitive data with the PyInstaller library  
isn't possible at the moment due to the error `keyring.errors.NoKeyringError` and since   
it has been like this for a long time now, I've decided to try to bind the Rust programming language  
keyring library (as I'm still learning it) to Python and been able to do so successfully.

Tested successfully on Windows 10 to work with PyInstaller.

# Installation

`pip install rskeyring`

**Please Note:** This currently works only on Windows.  
If you do not intend on using _PyInstaller_, do consider  
alternative keyring library such as:

`pip install keyring`


# Usage

## Store Password
```python
import rskeyring
from getpass import getpass

username = input("Username: ")
password = getpass()

rskeyring.set_password("service", username, password)
```

## Retrieve Password
```python
import rskeyring

username = input("Username: ")
password = rskeyring.get_password("service", username)

print(password)
```

## Delete Password
```python

import rskeyring

username = input("Username: ")
password = rskeyring.delete_password("service", username)

```

## Exceptions
Currently the external Rust `kerying-rs` library doesn't provide much of error details.  
So at this stage, we just throw a general `Exception` with a general error message originated by the underlying Rust library itself.  
* e.g. `Exception: Windows Vault Error`

# Compile
In order to compile the Rust code, you'll need to have the `rustup` toolchain.  
To install the `rustup` toolchain, go to https://rustup.rs

From within this directory, execute the next command to compile:  
`cargo build --release`

# Use Compiled Library

## Windows
Copy the file `pyrust-keyring\target\release\rskeyring.dll` to your Python project. Make sure you rename its extension from `.dll` to `.pyd`.

## MacOS
Copy the file `pyrust-keyring/target/release/rskeyring.dylib` to your Python project. Make sure you rename its extension from `.dylib` to `.so`.

# Docs

`help(rskeyring)`



