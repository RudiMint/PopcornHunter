from prompt_toolkit.completion import WordCompleter

from db_queries.history_query import get_top_queries, get_last_unique_queries
from db_queries.movie_service import movie_query, get_genres, get_year_range
from services.mongo_history_logs import log_search
from utils.mysql_connection import connection
from utils.mongo_connection import users
from ui.rich_views import (
    show_unique_queries,
    show_top_queries,
    show_year_range,
    show_genres_table,
    # show_genres,
    console,
    loading
)

GENRES = get_genres(connection)
MIN_YEAR, MAX_YEAR = get_year_range(connection)


COMMANDS = [
    "--tag",
    "--genre",
    "--year_range",
    "--top",
    "--unique",
    "--filter",
    "--help",
    "--quit"
]

command_completer = WordCompleter(COMMANDS, ignore_case=True)


def show_filters():

    show_genres_table(GENRES)
    show_year_range(MIN_YEAR, MAX_YEAR)

@log_search
def search_movies(arguments):
    query, params = movie_query(arguments)

    with loading("Searching movies..."):
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()

    return result


def show_history_stats(arguments, limit):

    if arguments.top:

        data = get_top_queries(users, limit)
        show_top_queries(data)
        return data

    elif arguments.unique:

        data = get_last_unique_queries(users, limit)
        show_unique_queries(data)
        return data




