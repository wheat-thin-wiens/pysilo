import os
import platform
from . import save_store

global ope
ope = platform.system()

def exe_venv(data_name: str):
    match ope:
        case "Windows":
            basedir = "C:/Users/Public"
            os.chdir(basedir)
        case "Darwin":
            basedir = "~/.local/share/python-venv"
            os.chdir(basedir)
        case "Linux":
            basedir = "~/.local/share/python-venv"
            os.chdir(basedir)

    venv_path = save_store.get_path(ope, data_name)
    script_path = os.path.join(venv_path, '/bin/activate')

    print(f"Initializing virtual environment at {venv_path}", end = ' ')
    os.system(f"python3 -m venv {venv_path}")
    print('Done.')

    print(f"Running activate script", end = ' ')
    os.system(f"source {script_path}")
    print('Done.')
