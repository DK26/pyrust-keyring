import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rskeyring-dk26",
    version="0.1.0",
    author="David Krasnitsky",
    author_email="dikaveman@gmail.com",
    description="A C-level keyring module ported from the Rust programming language (crates.io)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DK26/pyrust-keyring",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.8',
)