from prompt_toolkit.completion import WordCompleter

from db_queries.movie_service import movie_query, get_genres, get_year_range, execute_query
from db_queries.history_query import get_top_queries, get_last_unique_queries
from services.mongo_history_logs import log_search
from utils.mysql_connection import get_connection
from utils.mongo_connection import users
from ui.rich_views import (
    show_unique_queries,
    show_top_queries,
    show_year_range,
    show_genres_table,
    loading
)

with get_connection() as connection:
    GENRES = get_genres(connection)
    MIN_YEAR, MAX_YEAR = get_year_range(connection)


COMMANDS = [
    "--tag",
    "--genre",
    "--year_range",
    "--top_queries",
    "--unique",
    "--filter",
    "--help",
    "--quit"
]

command_completer = WordCompleter(COMMANDS, ignore_case=True)


def show_filters():
    """Display available filtering options for movie search."""
    show_genres_table(GENRES)
    show_year_range(MIN_YEAR, MAX_YEAR)


@log_search
def search_movies(arguments):
    """
    Execute a movie search query and return matching results from the database.
    :param arguments: Parsed CLI arguments containing search filters.
    :return: List of matching movie records, typically tuples in the form:
             (film_id, title, release_year, description)
    """
    query, params = movie_query(arguments)

    with loading("Searching movies..."):
        return execute_query(query, params)


def show_history_stats(arguments, limit):
    """
    Display search history statistics based on CLI arguments.
    :param arguments: Parsed CLI arguments containing history flags.
    :param limit: Maximum number of records to retrieve.
    :return: List of history records corresponding to the selected mode,
             or None if no valid option is selected.
    """

    if arguments.top_queries:

        data = get_top_queries(users, limit)
        show_top_queries(data)
        return data

    elif arguments.unique:

        data = get_last_unique_queries(users, limit)
        show_unique_queries(data)
        return data




