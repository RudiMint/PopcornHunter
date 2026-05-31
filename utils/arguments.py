import argparse
import shlex


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
    type=int,
    help="year or year range"
)
parser.add_argument(
    "--top",
    type=int,
    nargs="?",
    const=5,
    help="top requests, default 5"
)
parser.add_argument(
    "--unique",
    type=int,
    nargs="?",
    const=3,
    help="get last unique requests, default limit: 3"
)
parser.add_argument(
    "--quit",
    action="store_true",
    help="exit program"
)


def parse_command(command: str):
    return parser.parse_args(shlex.split(command))
