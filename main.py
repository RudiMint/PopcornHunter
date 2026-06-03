from prompt_toolkit import prompt
from rich.panel import Panel

from ui.cli import show_filters, search_movies, show_history_stats, command_completer
from ui.rich_views import console
from utils.arguments import parse_command, print_help
from utils.mysql_connection import connection
from utils.mongo_connection import client
from utils.paginator import Paginator


def main():
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
            print(args)

            if args.quit:
                break

            if args.help:
                print_help()
                continue

            if args.filters:
                show_filters()

            if args.top or args.unique:
                show_history_stats(args, limit=5)

            elif args.tag or args.genre or args.year_range:
                films = search_movies(args)
                if not films:
                    print("No results found")
                else:
                    paginator = Paginator(films, page_size=5)
                    paginator.run()

        except SystemExit:
            pass


if __name__ == "__main__":
    try:
        main()
    finally:
        client.close()
        connection.close()

