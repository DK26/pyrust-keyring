from setuptools import setup
from setuptools import find_packages
from setuptools_rust import Binding
from setuptools_rust import RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rskeyring",
    version="0.1.2.2",
    author="David Krasnitsky",
    author_email="dikaveman@gmail.com",
    description="A C-level keyring module bind from the Rust programming language (crates.io)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DK26/pyrust-keyring",
    rust_extensions=[RustExtension("rskeyring.rskeyring", binding=Binding.RustCPython)],
    packages=["rskeyring"] + find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
    zip_safe=False
)
