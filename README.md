## rskeyring (Rust Keyring)
A C-level, Rust keyring library bind to Python (https://github.com/DK26/pyrust-keyring).  
The Rust library (crate) itself was created by hwchen (https://github.com/hwchen/keyring-rs).

## Motivation
Since using _pypi.org_ keyring library to store sensitive data with the PyInstaller library  
isn't possible at the moment due to the error `keyring.errors.NoKeyringError` and since   
it has been like this for a long time now, I've decided to try to bind the Rust programming language  
keyring library (as I'm still learning it) to Python and been able to do so successfully.

Tested successfully on Windows 10 to work with PyInstaller.

## Installation

`pip install rskeyring`

## Usage

### Store or Update Password
```python
import rskeyring
from getpass import getpass

username = input("Username: ")
password = getpass()

try:
    rskeyring.set_password("service", username, password)
except OSError:
    print(f"Unable to create or update service for {username}."
        f"\nPlease make sure you have the proper permissions")
```

### Retrieve Password
```python
import rskeyring

username = input("Username: ")
try:
    password = rskeyring.get_password("service", username)
    print(password)
except OSError:
    print(f"Unable to get {username}'s password from 'service'")
```

### Delete Password
```python
import rskeyring

username = input("Username: ")

try:
    rskeyring.delete_password("service", username)
except OSError:
    print(f"Unable to remove {username} from 'service'")
```

### Exceptions
Currently the external Rust `kerying-rs` library doesn't provide any concrete error details.  
At this stage, we just throw a general `OSError` with an error message originated by the underlying Rust library itself.  
* e.g. `OSError: Windows Vault Error`


## Unit Tests

`python -m unittest tests.lib_unittest`



## Manual Use of Compiled Library

The `setuptools_rust` should be able to automatically compile & copy the rust libraries upon calling `pip install rskeyring`. 

If you wish to compile and import the Rust libraries to your python setup manually, please refer to the following notes:

### Compile
In order to compile the Rust code, you'll need to have the `rustup` toolchain.  
To install the `rustup` toolchain, go to https://rustup.rs

From within this directory, execute the next command to compile:  
`cargo build --release`

### Windows
Copy the file `pyrust-keyring\target\release\rskeyring.dll` to your Python project. Make sure you rename its extension from `.dll` to `.pyd`.

### MacOS
Copy the file `pyrust-keyring/target/release/rskeyring.dylib` to your Python project. Make sure you rename its extension from `.dylib` to `.so`.

## Docs

`help(rskeyring)`



