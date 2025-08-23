import subprocess
import importlib
import sys

__version__="0.1.1"

def show():
    print("pylib-T", __version__)

def testImport(library:str):
    if library in sys.modules:
        print(f"Library {library} is already imported.")
        return True

    try:
        # Using check=False so that a non-zero exit code does not raise a CalledProcessError
        returnmsg = subprocess.run(['pip', 'show', f'{library}'], capture_output=True, text=True, check=False)
        if (returnmsg.returncode != 0):
            print(f"Package {library} is not installed. Trying to install it...")
            installmsg = subprocess.run(['pip', 'install', f'{library}'], capture_output=True, text=True, check=False)
            if installmsg.returncode != 0:
                print(f"Failed to install library {library}.")
                return False # Return False if installation fails
        else:
            print(f"Library {library} is already installed. Trying to import it...")

        try:
            imported_module = importlib.import_module(library)
        except:
            print(f"Failed to import library {library}.")
            return False # Return False if import fails

        print(f"Successfully imported module: {library}") # Added a success message
        return True # Return True if import is successful

    except ImportError:
        print(f"Library {library} is NOT installed and could not be imported.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return False # Return False for any other exception

if __name__ == '__main__':
    show()