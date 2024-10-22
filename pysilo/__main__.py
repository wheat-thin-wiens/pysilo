import sys
from .cli import get_command_line_args
from .save_store import list_venvs, reg_cur_venv, reg_new_venv
from .venv import exe_venv

def main():
    args = get_command_line_args()
    venvs = list_venvs()

    if args.list:
        for key, value in venvs.items():
            print(f"{key}: {value}")
    elif args.register:
        reg_cur_venv()
    elif args.add:
        reg_new_venv()
    elif args.dir:
        exe_venv(args.dir)

if __name__ == '__main__':
    main()
