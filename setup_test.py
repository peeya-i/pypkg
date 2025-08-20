"""
from setuptools import setup, find_packages

setup(
    name="pypkg",
    version="0.1.4",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pypkg_a = pypkg.pylib_a:show',
            'pypkg_b = pypkg.pylib_b:show',
        ]
    }
)
"""