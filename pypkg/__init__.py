import subprocess
import importlib

__version__="0.1.1"

def show():
    print("pylib-T", __version__)

def testImport(library:str):
try:
    # Using check=False so that a non-zero exit code does not raise a CalledProcessError
    returnmsg = subprocess.run(['pip', 'show', f'{library}'], capture_output=True, text=True, check=False)
    if (returnmsg.returncode != 0):
        print(f"Library {library} is not installed. Trying to install it...")
        subprocess.run(['pip', 'install', f'{library}'], capture_output=True, text=True, check=True)
    imported_module = importlib.import_module(library)
    print(f"Successfully imported module: {library}") # Added a success message

except ImportError:
    print(f"Library {library} is NOT installed and could not be imported.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    show()