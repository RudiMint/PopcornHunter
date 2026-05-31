def get_top_queries(collection, limit):
    pipeline = [
        {
            "$group": {
                "_id": "$search_type",
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


def get_last_unique_queries(collection, limit):
    pipeline = [
        {
            "$sort": {"timestamp": -1}
        },
        {
            "$group": {
                "_id": "$search_type",
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

