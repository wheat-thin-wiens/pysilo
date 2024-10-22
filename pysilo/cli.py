from . import __version__
from .venv import exe_venv
from .save_store import list_venvs
import argparse

from pysilo import save_store

def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog = "Python venv launch tool",
        description = "Small CLI tool for managing Python venvs with Bash shell",
    )

    parser.add_argument(
        'dir',
        type = str,
        nargs = '?',
        default = 'Default',
        choices = list_venvs(),
        help = 'Activates selected environment'
    )

    parser.add_argument(
        '-v',
        '--version',
        action = "version",
        version = __version__,
        help = 'Show version'
    )

    parser.add_argument(
        '-r',
        '--register',
        action = 'store_true',
        help = 'Register current venv',
    )
    
    parser.add_argument(
        '-a',
        '--add',
        action = 'store_true',
        help = 'Register new venv',
    )

    parser.add_argument(
        '-l',
        '--list',
        action = 'store_true',
        help = 'List all registered venvs'
    )

    parser.add_argument(
        '-d',
        '--deactivate',
        action = 'store_true',
        help = 'Deactivate current venv',
    )

    return parser.parse_args()

