import argparse

from rich.console import Console

from utils.command_splitter import input_split

console = Console()


class RichArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        console.print("\n[bold red]❌ Argument error[/bold red]")
        console.print(f"[red]{message}[/red]\n")

        console.print("[yellow]💡 Example:[/yellow]")
        console.print("  --genre Action Comedy")
        console.print("  --tag space future\n")

        console.print("[cyan]Tip:[/cyan] use --help for full command list\n")

        raise SystemExit(1)

parser = RichArgumentParser(add_help=False)

def parse_command(command: str):
    return parser.parse_args(input_split(command))

def print_help():
    console.print("""
[bold cyan]📌 PopcornHunter CLI[/bold cyan]

[green]Search movies:[/green]
  --genre Action Comedy
  --tag space future
  --year_range 2000 2010

[green]History:[/green]
  --top
  --unique

[green]System:[/green]
  --quit
""")

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

parser.add_argument(
    "-h",
    "--help",
    action="store_true"
)


