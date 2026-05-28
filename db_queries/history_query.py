# from utils.mongo_connection import users
def get_top_queries(collection, limit=5):
    pipeline = [
        {
            "$group": {
                "_id": "$params",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": limit
        }
    ]

    return list(collection.aggregate(pipeline))


def get_last_unique_queries(collection, limit=3):
    pipeline = [
        {
            "$sort": {"timestamp": -1}
        },
        {
            "$group": {
                "_id": "$params",
                "timestamp": {"$first": "$timestamp"}
            }
        },
        {
            "$sort": {"timestamp": -1}
        },
        {
            "$limit": limit
        }
    ]
    return list(collection.aggregate(pipeline))

# result = get_top_queries(users, limit=3)
#
# for item in result:
#     print(f"{item['_id']} -> {item['count']}")
