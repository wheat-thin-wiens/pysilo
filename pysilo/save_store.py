import json
import os
import platform
import sys

global ope, home, file_name, file_path

ope = platform.system()
file_name = f"{ope}.json"

match ope:
    case "Windows":
        file_path = "C:/Users/Public"
    case "Darwin":
        home = os.path.expanduser('~')
        file_path = os.path.join(home, '.config/pysilo')
    case "Linux":
        home = os.path.expanduser('~')
        file_path = os.path.join(home, '.config/pysilo')

def get_path(data_name: str) -> str:
    os.chdir(file_path)     # type: ignore

    try: 
        with open(file_name, 'r') as file:
            data = json.load(file)
            path = data.get(data_name)

        return path

    except ValueError:
        return 'Not Registered'

    except FileNotFoundError:
        json_init()
        return get_path(data_name)

def write_path(new_data: dict):
    os.chdir(file_path)
    key, value = list(new_data.items())[0]

    if '~' in value:
        fixed_dir = os.path.expanduser('~')
        value = value.replace('~', fixed_dir)
        new_data = {key: value}

    with open(file_name, 'r') as file:
        data = json.load(file)
        data.update(new_data)

    with open(file_name, 'w') as file:
            json.dump(data, file, indent = 4)

def json_init():
    if not os.path.isdir(file_path):
        print(f"Creating {file_path}")
        os.mkdir(file_path)
    else:
        print(f"{file_path} found.")

    os.chdir(file_path)

    if not os.path.isfile(file_name):
        print(f"Creating {file_name}")
        open(file_name, 'x')
        with open(file_name, 'w') as file:
            json.dump({}, file, indent = 4)
    else:
        print(f"{file_name} found.")

def reg_cur_venv():
    curd = sys.prefix
    name = input("Enter a name for this environment >  ")
    write_path({name: curd})
    return

def reg_new_venv():
    name = input("Enter a name for this environment >  ")
    location = input('Enter the location of this environment > ')
    write_path({name: location})

def list_venvs():
    os.chdir(file_path)
    with open(file_name, 'r') as file:
        data = json.load(file)

    venvs = [key for key in data.keys()]
    verbose_venvs = {}

    for key, value in data.items():
        verbose_venvs.update({key: value})
    
    return verbose_venvs
