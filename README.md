# pyrust-keyring
A C-level convertion to Python (cpython) of the Rust keyring crate by hwchen (https://github.com/hwchen/keyring-rs).

# Motivation
Since using keyring to store sensitive data with the PyInstaller library isn't possible at the moment due a long-term error in the process, I've decided to attempt a convertion from the Rust programming language (as I'm still learning it) of its own keyring library to Python.

Tested succesfully on Windows 10.

# Compile
`cargo build --release`

# Use Compiled Library
Copy the file `pyrust-keyring\target\release\rskeyring.dll` to your Python project. Make sure you rename its extension from `.dll` to `.pyd`.

# Usage
```python
import rskeyring

rskeyring.set_password("service", "user", "password")

secret = rskeyring.get_password("serivce", "user")

print(secret)
```

# Docs

`help(rskeyring)`



