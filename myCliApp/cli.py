import sys
import argparse
from colors import *
from myCliApp.globals import app_version, app_name


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog=app_name,
        description="Text describing the atlas application.",
        epilog="Text at the bottom of help",
    )

    parser.add_argument(
        "-v",
        "--version",
        help="prints the applications version",
        action="version",
        version=f"%(prog)s {app_version}",
    )

    return parser.parse_args()


def cli():
    try:
        args = parse_arguments()

        # Add application code here
        print(color(f"{app_name} v{app_version}", fg="blue"))

    except KeyboardInterrupt:
        print("Aborted by user.")
        sys.exit(0)


if __name__ == "__main__":
    cli()
