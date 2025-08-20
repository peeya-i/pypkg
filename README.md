# PyPkg
Testing multi library package.

## To use pyproject.toml
There are 3libraries in this package. To install the package, use the following command:
```
pip install git+https://github.com/peeya-i/pypkg.git
```
To import use the following command. Each library is imported independently.
```
import pypkg
import pypkg.pylib_a
import pypkg.pylib_b
```

The Package version is in pyproject.toml
The version for pypkg library is in pypkg/__init__.py
The version for pypkg.pylib_a library is in pypkg/pylib_a/__init__.py
The version for pypkg.pylib_b library is in pypkg/pylib_b/__init__.py

The folder pypkg1 can't be accessed because it is not part of the 

## To set up using setup.py - still being tested
```
python setup.py sdist bdist_wheel
twine upload dist/*
```