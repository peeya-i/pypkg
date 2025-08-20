# PyPkg
Testing multi library package.

## To use pyproject.toml
```
pip install git+https://github.com/peeya-i/pypkg.git

import pypkg
import pypkg.pylib_a
import pypkg.pylib_b
```

## To set up using setup.py
```
python setup.py sdist bdist_wheel
twine upload dist/*
```
To use:
```
pip install pypkg
```