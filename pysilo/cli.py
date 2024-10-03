import argparse

def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog = "Python venv launch tool",
        description = "Small CLI tool for managing Python venvs with Bash shell",
    )

    parser.add_argument(
        '-v',
        '--version',
        action = "version",
        version = __version__
    )

    parser.add_argument(
        '-d',
        '--default',
        action = venv.exe_venv('Default')
    )
    
    parser.add_argument(
        '-r',
        '--register',
    )
    
    parser.add_argument(
        '-a',
        '--add',
    )

    return parser.parse_args()
