from db_queries.history_query import get_top_queries, get_last_unique_queries
from db_queries.movie_service import movie_query, get_genres, get_year_range
from services.mongo_history_logs import log_search
from utils.mysql_connection import connection
from utils.mongo_connection import users
# from difflib import get_close_matches

GENRES = get_genres(connection)
MIN_YEAR, MAX_YEAR = get_year_range(connection)


def show_filters():
    print("\npossible genre options:\n")

    for genre in GENRES:
        print("-", genre)

    print(
        f"\npossible year range:\n"
        f"{MIN_YEAR} - {MAX_YEAR}"
    )


@log_search
def search_movies(arguments):
    query, params = movie_query(arguments)

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()

        return result


def show_history_stats(arguments, limit):

    if arguments.top:
        top_queries = get_top_queries(users, limit)
        print("\ntop queries:")

        for item in top_queries:
            print(
                f"{item['_id']} "
                f"({item['count']} раз)"
            )
        return top_queries

    elif arguments.unique:
        unique_queries = get_last_unique_queries(users, limit)
        print("\nlast unique queries:")

        for item in unique_queries:
            print(item["_id"])

        return unique_queries



# suggestions = get_close_matches(args.genre, GENRES, n=3)
# print(suggestions)
#
# def user_communication(args):
#     print("all genres to pick: ")


