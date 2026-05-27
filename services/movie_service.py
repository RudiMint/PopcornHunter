def build_query(*args):
    query = """
        SELECT f.*
        FROM film f
        LEFT JOIN film_category fc on f.film_id = fc.film_id
        LEFT JOIN category c on fc.category_id = c.category_id
    """

    conditions = []
    params = []

    if args.tag:
        conditions.append("(f.title LIKE %s OR f.description LIKE %s)")
        params.append(f"%{args.tag}%")
        params.append(f"%{args.tag}%")

    if args.genre:
        genre_list = []
        for g in args.genre:
            genre_list.append("c.name = %s")
            params.append(g)
        conditions.append("(" + " OR ".join(genre_list) + ")")

    if args.year_range:

        if len(args.year_range) == 1:
            conditions.append("f.release_year = %s")
            params.append(args.year_range[0])

        elif len(args.year_range) >= 2:
            conditions.append("f.release_year BETWEEN %s AND %s")
            params.append(args.year_range[0])
            params.append(args.year_range[1])

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    limit = 10
    query += " ORDER BY f.rental_rate DESC LIMIT %s"
    params.append(limit)

    return query, params


