
__version__="0.1.1"

def show():
    print("pylib-T", __version__)

def testImport(library:str):
    try:
        a = subprocess.run(['pip', f'{library}'], capture_output=True, text=True, check=True)
        subprocess.run(['pip', 'install', f'{library}'], capture_output=True, text=True, check=True)
        import f'{library}'
    except ImportError:
        print(f"Library {library} is NOT installed.")
    if 
    import pypkg.pylib_a


if __name__ == '__main__':
    show()