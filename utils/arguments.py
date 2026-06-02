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

[bold green]🎬 Search movies[/bold green]
  --genre Action Comedy
      Search movies by one or more genres

  --tag space future
      Search by keywords in title or description

  --year_range 2000 2010
      Filter movies by year or year range

[bold yellow]📊 History[/bold yellow]
  --top
      Show most frequent search queries

  --unique
      Show last unique search types

[bold magenta]🔧 System[/bold magenta]
  --filters
      Show all available genres and year range

  --quit
      Exit the application

[bold blue]💡 Tips[/bold blue]
  • You can combine filters: --genre Drama --year_range 2000 2010
  • Multiple values allowed: --genre Action Comedy
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
    "--filters",
    action="store_true",
    help="show all available filters"
)

parser.add_argument(
    "-h",
    "--help",
    action="store_true"
)


