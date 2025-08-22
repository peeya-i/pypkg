import subprocess
import importlib

__version__="0.1.1"

def show():
    print("pylib-T", __version__)

def testImport(library:str):
    try:
        returnmsg = subprocess.run(['pip', 'show', f'{library}'], capture_output=True, text=True, check=True)
        if (returnmsg.returncode != 0):
            print(f"Library {library} is not installed. Trying to install it...")
            subprocess.run(['pip', 'install', f'{library}'], capture_output=True, text=True, check=True)
        imported_module = importlib.import_module(library)
    except ImportError:
        print(f"Library {library} is NOT installed.")


if __name__ == '__main__':
    show()