import os
import platform
from . import save_store

global ope
ope = platform.system()

def exe_venv(data_name: str):
    match ope:
        case "Windows":
            basedir = "C:/Users/Public"
            py_command = 'python'
            os.chdir(basedir)
        case "Darwin":
            basedir = "~/.local/share/python-venv"
            py_command = 'python3'
            os.chdir(basedir)
        case "Linux":
            basedir = "~/.local/share/python-venv"
            py_command = 'python3'
            os.chdir(basedir)

    venv_path = save_store.get_path(data_name)
    script_path = os.path.join(venv_path, '/bin/activate')

    print(f"Initializing virtual environment at {venv_path}", end = ' ')
    os.system(f"{py_command} -m venv {venv_path}")     # type: ignore
    print('Done.')

    print(f"Running activate script", end = ' ')
    os.system(f"source {script_path}")
    print('Done.')
