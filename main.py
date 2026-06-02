from ui.cli import show_filters, search_movies, show_history_stats
from utils.mysql_connection import connection
from utils.mongo_connection import client
from utils.arguments import parse_command
from utils.paginator import Paginator


def main():
    print("Wellcome to Popcorn Hunter\n")
    show_filters()
    while True:
        command = input("> ")
        try:
            args = parse_command(command)
            print(args)

            if args.quit:
                break

            if args.top or args.unique:
                show_history_stats(args, limit=5)

            elif args.tag or args.genre or args.year_range:
                films = search_movies(args)
                paginator = Paginator(films, page_size=5)
                paginator.run()

        except SystemExit:
            print("Invalid command")


if __name__ == "__main__":
    try:
        main()
    finally:
        client.close()
        connection.close()

