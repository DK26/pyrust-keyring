use cpython::{Python, PyResult, PyObject, exc, PyErr, py_module_initializer, py_fn};

py_module_initializer!(rskeyring, |py, m | {

    let _doc =
    r#"A C-level keyring module bound from the Rust programming language.

        This is a "keyring" library for storing sensitive data, that is borrowed and bound from
         another open-source library (keyring-rs) that is written in the Rust programming language,
         a new & exciting C-level programing language.

        The main motivation behind creating this bind was to enable keyring with the PyInstaller
         tool, since the most rated Pypi.org keyring library seem to have compatibilty issues with it.
         As the alternatives & workarounds were not as secure, I have decided to check what is the
         most rated crates.io (Rust) library ("crate") that could do the job and chose "keyring-rs".

        This also provided me with an excuse and a chance to learn about binding rust to python.

        Rust Keyring Library(Crate):

            https://docs.rs/crate/keyring

        GitHub Respositories:

            Rust Keyring (keyring-rs):     https://github.com/hwchen/keyring-rs

                Copyright (c) 2017 keyring developers

            Python Bind (rskeyring):       https://github.com/DK26/pyrust-keyring

                Copyright (c) 2020 David Krasnitsky

        Licenses:

            Python Bind (rskeyring): MIT

            Rust Keyring (keyring-rs): MIT + Apache 2.0"

        Contact:

            E-mails:    dikaveman@gmail.com,

                        dave@cybersiem.com

            GitHub:     https://github.com/DK26

        Version: 0.1.1"#;

    m.add(py, "__doc__", _doc)?;
    m.add(py, "set_password", py_fn!(py, set_password(service: &str, username: &str, password: &str)))?;
    m.add(py, "get_password", py_fn!(py, get_password(service: &str, username: &str)))?;
    m.add(py, "delete_password", py_fn!(py, delete_password(service: &str, username: &str)))?;
    Ok(())
});

fn set_password(_py: Python, service: &str, username: &str, password: &str) -> PyResult<PyObject> {

    let keyring_service = keyring::Keyring::new(service, username);

    match keyring_service.set_password(password) {
        Ok(()) => Ok(_py.None()),
        Err(_e) => Err(PyErr::new::<exc::OSError, _>(_py, _e.to_string()))
    }
}

fn get_password(_py: Python, service: &str, username: &str) -> PyResult<String> {

    let keyring_service = keyring::Keyring::new(service, username);

    return match keyring_service.get_password()
    {
        Ok(result) => Ok(result),
        Err(_e) => Err(PyErr::new::<exc::OSError, _>(_py, _e.to_string()))
    }

}


fn delete_password(_py: Python, service: &str, username: &str) -> PyResult<PyObject> {

    let keyring_service = keyring::Keyring::new(service, username);

    match keyring_service.delete_password()
    {
        Ok(_) => Ok(_py.None()),
        Err(_e) => Err(PyErr::new::<exc::OSError, _>(_py, _e.to_string()))
    }

}