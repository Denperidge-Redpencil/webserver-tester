# Built-in imports
from sys import argv
from argparse import ArgumentParser


with open("README.md", "r", encoding="utf-8") as file:
    description = file.readlines()[1]

parser = ArgumentParser(
    prog="webserver-tester",
    description=description
)

parser.add_argument("--all", action="store_true", help="When passed, uses all available testing tools")
parser.add_argument("--show-testers", action="store_true", help="When passed, list all available testing tools")

# Thanks to https://stackoverflow.com/a/47440202
args = parser.parse_args(args=argv[1:] or ["--help"])


use_all_testers: bool = args.all
"""Whether to use all available testers"""

show_all_testers: bool = args.show_testers
"""Whether to show all available testers"""