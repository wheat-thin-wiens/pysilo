import json
import os
import platform

global ope, home, file_name, file_path

ope = platform.system()
file_name = 'pysilo.json'

match ope:
    case "Windows":
        file_path = "C:/Users/Public"
    case "Darwin":
        home = os.path.expanduser('~')
        file_path = os.path.join(home, '.config/pysilo')
    case "Linux":
        home = os.path.expanduser('~')
        file_path = os.path.join(home, '.config/pysilo')

def get_path(system: str, data_name: str):
    os.chdir(file_path)     # type: ignore

    try: 
        with open(file_name, 'r') as file:
            system_data = json.load(file)
            read_data = system_data.get(system)

        match read_data:
            case None:
                print(f"{data_name} is not saved.")
                return ''
            case _:
                return read_data
    except ValueError:
        return ''

def check_for_dir():
    try:
        os.chdir(file_path)
        print('File path found')
    except FileNotFoundError:
        os.mkdir(file_path)
        print(f"Created file path: {file_path}")

def check_for_file():
    os.chdir(file_path)

    if os.path.isfile(file_name):
        print("File found")
        return
    else:
        os.system(f"touch {file_name}")
        with open(file_name, 'w') as file:
            data = {
                "Windows": {},
                "Darwin": {},
                "Linux": {}
            }
            json.dump(data, file, indent = 4)
        print(f"JSON not found, creating file in {file_path}")    # type: ignore
        return

