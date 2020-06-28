#!/bin/bash
set -ex

PY3=$(command -v python3)
PY3_HOME=$(dirname "$PY3")

curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain stable -y
export PATH="$HOME/.cargo/bin:$PATH"

#cd /io

"${PY3_HOME}/pip3" install -U setuptools wheel setuptools-rust
"${PY3_HOME}/python3" setup.py bdist_wheel

#for PYBIN in ${PY3_HOME}/{cp27-cp27m,cp27-cp27mu,cp35-cp35m,cp36-cp36m,cp37-cp37m}/bin; do
#    export PYTHON_SYS_EXECUTABLE="$PYBIN/python"
#
#    "${PY3_HOME}/pip3" install -U setuptools wheel setuptools-rust
#    "${PY3_HOME}/python3" setup.py bdist_wheel
#done

for whl in dist/*.whl; do
    auditwheel repair "$whl" -w dist/
done
