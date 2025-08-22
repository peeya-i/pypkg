from .randomclass import random as rd1
# Not import random2 to test whether it will show up after importing
import subprocess

__version__="0.1.3"

def show():
    print("pylib-b", __version__)
    rd1(10)

def show2():
    print("pylib-b show2")

if __name__ == '__main__':
    show()