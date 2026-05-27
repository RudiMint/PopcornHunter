import argparse


parser = argparse.ArgumentParser()


parser.add_argument(
    "--tag",
    required=True,
    type=str,
    help="name of the film or keyword/s in quotation marks"
)
parser.add_argument(
    "--genre",
    required=True,
    nargs="+",
    help="one or more genres")
parser.add_argument(
    "--year_range",
    required=True,
    nargs="+",
    type=int,
    help="year or year range"
)
parser.add_argument(
    "--top",
    required=True,
    default=5,
    type=int,
    help="top requests, default 5"
)
