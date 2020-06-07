# pyrust-keyring
A C-level conversion to Python (cpython) of the Rust keyring crate by hwchen (https://github.com/hwchen/keyring-rs).

# Motivation
Since using keyring to store sensitive data with the PyInstaller library isn't possible at the moment,
 and since it has been like that for a long while now, I've decided to attempt a conversion from the Rust programming language 
keyring library (as I'm still learning it) to Python.

Tested successfully on Windows 10 with PyInstaller.

# Compile
`cargo build --release`

# Use Compiled Library

## Windows
Copy the file `pyrust-keyring\target\release\rskeyring.dll` to your Python project. Make sure you rename its extension from `.dll` to `.pyd`.

## MacOS
Copy the file `pyrust-keyring/target/release/rskeyring.dylib` to your Python project. Make sure you rename its extension from `.dylib` to `.so`.


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

# Docs

`help(rskeyring)`



