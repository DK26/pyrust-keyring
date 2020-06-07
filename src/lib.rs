use cpython::{Python, PyResult, PyObject, py_module_initializer, py_fn};

py_module_initializer!(rskeyring, |py, m | {
    m.add(py, "__doc__", "A keyring module imported from the Rust programming language. \n\
    Rust Keyring Library(Crate): https://docs.rs/crate/keyring\n\
    The main motivation behind this port is to enable keyring with PyInstaller.")?;
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