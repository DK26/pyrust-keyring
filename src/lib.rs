use cpython::{Python, PyResult, PyObject, py_module_initializer, py_fn};

py_module_initializer!(rskeyring, |py, m | {

    let _doc =
    r#"A C-level keyring module ported from the Rust programming language.

        The main motivation behind creating this port was to enable keyring with PyInstaller.

        Rust Keyring Library(Crate):
            https://docs.rs/crate/keyring

        GitHub Respositories:
            Rust Keyring: https://github.com/hwchen/keyring-rs
            Python Port: https://github.com/DK26/pyrust-keyring

        Rust Keyring (keyring-rs) Copyright 2017 keyring developers

        Python Port by David Krasnitsky <dikaveman@gmail.com>, <dave@cybersiem.com>
            GitHub: https://github.com/DK26

        Licenses:
            Python Port: MIT
            Rust Keyring (keyring-rs): MIT + Apache 2.0"#;

    m.add(py, "__doc__", _doc)?;
    m.add(py, "set_password", py_fn!(py, set_password(service: &str, username: &str, password: &str)))?;
    m.add(py, "get_password", py_fn!(py, get_password(service: &str, username: &str)))?;
    Ok(())
});

fn set_password(_py: Python, service: &str, username: &str, password: &str) -> PyResult<PyObject> {

    let keyring_service = keyring::Keyring::new(service, username);

    match keyring_service.set_password(password) {
        _ => {} // ignore returning values / errors
    }

    Ok(_py.None())
}

fn get_password(_py: Python, service: &str, username: &str) -> PyResult<String> {

    let keyring_service = keyring::Keyring::new(service, username);

    return match keyring_service.get_password()
    {

        Ok(result) => Ok(result),
        Err(_e) => Ok(String::new())
    }

}