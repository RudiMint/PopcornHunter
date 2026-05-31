import argparse
from utils.command_splitter import input_split


parser = argparse.ArgumentParser()


parser.add_argument(
    "--tag",
    type=str,
    nargs="+",
    help="one or more keywords (space separated)"
)
parser.add_argument(
    "--genre",
    type=str,
    nargs="+",
    help="one or more genres")
parser.add_argument(
    "--year_range",
    nargs="+",
    type=str,
    help="year or year range"
)
parser.add_argument(
    "--top",
    type=str,
    nargs="?",
    const=5,
    help="top requests, default 5"
)
parser.add_argument(
    "--unique",
    type=str,
    nargs="?",
    const=3,
    help="get last unique requests, default limit: 5"
)
parser.add_argument(
    "--quit",
    action="store_true",
    help="exit program"
)


def parse_command(command: str):
    return parser.parse_args(input_split(command))
