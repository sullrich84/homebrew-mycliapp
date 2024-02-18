import sys
import argparse
from myCliApp.version import __version__


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="MyCliApp",
        description="Text describing the atlas application.",
        epilog="Text at the bottom of help",
    )

    parser.add_argument(
        "-v",
        "--version",
        help="Prints the application version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser.parse_args()


def cli():
    try:
        args = parse_arguments()

        # Add application code here
        print("Hello World!")

    except KeyboardInterrupt:
        print("Aborted by user.")
        sys.exit(0)


if __name__ == "__main__":
    cli()
