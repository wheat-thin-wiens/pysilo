import os
import platform
import subprocess
import sys
from .save_store import get_path

global ope
ope = platform.system()

def exe_venv(data_name: str):
    match ope:
        case "Windows":
            py_command = 'python'
        case "Darwin":
            py_command = 'python3'
        case "Linux":
            py_command = 'python3'

    venv_path = get_path(data_name)
    # add_path = os.path.join(venv_path, 'bin')
    # script_path = os.path.join(venv_path, 'bin/activate')
    env = os.environ['PATH']

    print(env)
    print(type(env))

    # print(f"Initializing virtual environment at {venv_path}...", end = ' ')
    # os.system(f"{py_command} -m venv {venv_path}")     # type: ignore
    # subprocess.run([py_command, '-m', 'venv', venv_path], shell = False) # type: ignore
    # print('Done.')

    # print(f"Running activate script...", end = ' ')
    # os.system(f"source {script_path}")
    # exec(open(script_path).read(), {'__file__': script_path})
    # print('Done.')
    return

def deactivate():
    curd = sys.prefix
    env = os.environ['PATH']
    venv_path = os.path.join(curd, 'bin')
    


def process_path(path):
    copy = path.split('/')[1:]
    home_path = os.path.expanduser('~').split('/')[1:]
    if copy[:2] == home_path:
        copy = copy[2:]
    new_copy = '/'.join(copy)
    new_copy = os.path.join('~', new_copy)
    new_copy = os.path.join(new_copy, 'bin/activate')
