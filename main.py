from prompt_toolkit import prompt
from rich.panel import Panel

from ui.cli import show_filters, search_movies, show_history_stats, command_completer
from utils.arguments import parse_command, print_help
from utils.mongo_connection import client
from utils.paginator import Paginator
from ui.rich_views import console


def main():
    """
    Entry point for the PopcornHunter CLI application.

    This function initializes the CLI interface, displays the welcome screen,
    and runs the main interactive command loop.

    The loop continues until the user explicitly exits via the `--quit`
    command or equivalent argument.
    """
    console.print(Panel.fit(
        "[bold cyan] Popcorn Hunter[/bold cyan]\n"
        "[white]Movie search CLI[/white]",
        border_style="magenta"
    ))
    show_filters()
    print_help()

    while True:
        command = prompt("> ", completer=command_completer)
        try:
            args = parse_command(command)

            if args.quit:
                break

            if args.help:
                print_help()
                continue

            if args.filters:
                show_filters()

            if args.top_queries or args.unique:
                show_history_stats(args, limit=5)

            elif args.tag or args.genre or args.year_range:
                films = search_movies(args)
                if not films:
                    print("No results found")
                else:
                    paginator = Paginator(films, page_size=10)
                    paginator.run()

        except SystemExit:
            pass


if __name__ == "__main__":
    try:
        main()
    finally:
        client.close()

