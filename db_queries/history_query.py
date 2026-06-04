def get_top_queries(collection, limit):
    """
    Return the most frequently used search types from a MongoDB collection.

    :param MongoDB collection:
    :param limit:
    :return: List of aggregated results. Each item contains:
             - ``_id``: search type
             - ``count``: number of occurrences
             - ``doc``: most recent document for that search type
    """
    pipeline = [
        {
            "$sort": {"timestamp": -1}
        },
        {
            "$group": {
                "_id": "$search_type",
                "count": {"$sum": 1},
                "doc": {"$first": "$$ROOT"}
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
    """
    Return the last unique requests from a MongoDB collection.
    :param MongoDB collection:
    :param limit:
    :return: A list of dictionaries representing the most recent query for
             each unique search type.
    """
    pipeline = [
        {
            "$sort": {"timestamp": -1}
        },
        {
            "$group": {
                "_id": "$search_type",
                "doc": {"$first": "$$ROOT"}
            }
        },
        {
            "$sort": {"doc.timestamp": -1}
        },
        {
            "$limit": limit
        },
        {
            "$project": {
                "_id": 0,
                "search_type": "$_id",
                "timestamp": "$doc.timestamp",
                "params": {
                    "$arrayToObject": {
                        "$filter": {
                            "input": {"$objectToArray": "$doc.params"},
                            "as": "item",
                            "cond": {
                                "$and": [
                                    {
                                        "$not": {
                                            "$in": [
                                                "$$item.v",
                                                [None, True, False]
                                            ]
                                        }
                                    },
                                    {"$ne": ["$$item.v", None]},
                                    {"$ne": ["$$item.v", []]}
                                ]
                            }
                        }
                    }
                },
                "results_count": "$doc.results_count"
            }
        }
    ]

    return list(collection.aggregate(pipeline))
