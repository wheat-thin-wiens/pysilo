import os
import platform
from .save_store import get_path

global ope, home
ope = platform.system()

def exe_venv(data_name: str):
    match ope:
        case "Windows":
            # basedir = "C:/Users/Public"
            py_command = 'python'
            # os.chdir(basedir)
        case "Darwin":
            # home = os.path.expanduser('~')
            # basedir = os.path.join(home, '.config/pysilo')
            py_command = 'python3'
            # os.chdir(basedir)
        case "Linux":
            # home = os.path.expanduser('~')
            # basedir = os.path.join(home, '.config/pysilo')
            py_command = 'python3'
            # os.chdir(basedir)

    venv_path = get_path(data_name)
    script_path = os.path.join(venv_path, 'bin/activate')

    print(f"Initializing virtual environment at {venv_path}...", end = ' ')
    os.system(f"{py_command} -m venv {venv_path}")     # type: ignore
    print('Done.')

    print(f"Running activate script...", end = ' ')
    os.system(f"source {script_path}")
    print('Done.')
    return
