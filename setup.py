import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exchange-api",
    version="1.0.0",
    author="Cory Cline, Gabe Rust",
    description="A Framework for Abstracting Crypto-Currency Exchange APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaberust/exchange_api",
    license="LICENSE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
