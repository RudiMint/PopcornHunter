import argparse


parser = argparse.ArgumentParser()


parser.add_argument(
    "--tag",
    type=str,
    help="name of the film or keyword/s in quotation marks"
)
parser.add_argument(
    "--genre",
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
    default=5,
    type=int,
    help="top requests, default 5"
)
