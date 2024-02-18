import os
from setuptools import setup, find_packages


def get_version():
    rel_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(rel_path, "myCliApp", "version.py")

    v = {}
    with open(path) as fp:
        exec(fp.read(), v)

    return v["__version__"]


setup(
    name="myCliApp",
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    # Note: Align this with Homebrew formula!
    python_requires=">=3.9",
    # Required third party dependencies for this application
    # Note: Also define this in the Homebrew formula via poet!
    # Note: Also import this in __init__.py!
    install_requires=[
        "argparse==1.4.0",
    ],
    # Homebrew will use this to define the entry point
    # for the executable of this application.
    entry_points="""
        [console_scripts]
        myCliApp=myCliApp.cli:cli
    """,
)
