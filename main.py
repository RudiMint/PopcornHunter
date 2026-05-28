from db_queries.movie_service import movie_query
from utils.mysql_connection import connection
from services.mongo_history_logs import log_search
from utils.arguments import parser

args = parser.parse_args()


@log_search(search_type=args.mode)
def search_movies(**kwargs):
    query, params = movie_query(args)
    connection.cursor.execute(query, params)
    return connection.cursor.fetchall()


if __name__ == "__main__":

    try:
        results = search_movies(**vars(args))

        print(f"Found: {len(results)}")
        for r in results[:10]:
            print(r)
        if not results:
            print("Not found")

    except Exception as e:
        print("Error:", e)