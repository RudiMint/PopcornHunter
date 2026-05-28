# import argparse
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

        print("Log saved!")
        print("Inserted ID:", result.inserted_id)

        return result.inserted_id


logger = SearchLogger(users)

def log_search(search_type):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            keyword = kwargs.get("keyword") or args[0]

            # execute search
            results = func(*args, **kwargs)

            # log request
            logger.log(
                search_type=search_type,
                params=kwargs,
                results_count=len(results)
            )

            return results

        return wrapper

    return decorator




# @log_search("keyword")
# def search_items(keyword):
#
#     items = [
#         {"title": "python tutorial"},
#         {"title": "python mongodb"},
#         {"title": "argparse guide"},
#         {"title": "fastapi course"}
#     ]
#
#     return [
#         item
#         for item in items
#         if keyword.lower() in item["title"].lower()
#     ]
#
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("--keyword")
#
# args = parser.parse_args()
#
#
# results = search_items(args.keyword)
#
# print("\nResults:")
# print(results)