from datetime import datetime, timezone
from functools import wraps

from utils.mongo_connection import users

class SearchLogger:
    def __init__(self, collection):
        self.collection = collection

    def log(self, search_type, params, results_count):
        result = self.collection.insert_one({
            "timestamp": datetime.now(timezone.utc),
            "search_type": search_type,
            "params": params,
            "results_count": results_count
        })

        return result.inserted_id


logger = SearchLogger(users)


def log_search(func):

    @wraps(func)
    def wrapper(arguments):

        results = func(arguments)

        params = vars(arguments)

        search_parts = []

        if arguments.tag:
            search_parts.append("tag")
        if arguments.genre:
            search_parts.append("genre")
        if arguments.year_range:
            search_parts.append("year")

        search_type = "+".join(search_parts) if search_parts else "empty"

        logger.log(
            search_type=search_type,
            params=params,
            results_count=len(results or [])
        )

        return results

    return wrapper

