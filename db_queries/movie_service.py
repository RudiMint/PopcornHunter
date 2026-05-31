def movie_query(args):
    query = """
        SELECT f.*
        FROM film f
        LEFT JOIN film_category fc on f.film_id = fc.film_id
        LEFT JOIN category c on fc.category_id = c.category_id
    """

    conditions = []
    params = []

    if args.tag:
        tag_group = []
        for t in args.tag:
            tag_group.append("(f.title LIKE %s OR f.description LIKE %s)")
            params.extend([f"%{t}%", f"%{t}%"])

        conditions.append("(" + " OR ".join(tag_group) + ")")

    if args.genre:
        placeholders = ", ".join(["%s"] * len(args.genre))
        conditions.append(f"c.name IN ({placeholders})")
        params.extend(args.genre)

    if args.year_range:

        if len(args.year_range) == 1:
            conditions.append("f.release_year = %s")
            params.append(args.year_range[0])

        elif len(args.year_range) >= 2:
            start, end = args.year_range[:2]
            conditions.append("f.release_year BETWEEN %s AND %s")
            params.extend([start, end])

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    return query, params

def get_genres(conn):
    query = "SELECT name FROM category"

    with conn.cursor() as cursor:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]


def get_year_range(conn):
    query = """
        SELECT
            MIN(release_year),
            MAX(release_year)
        FROM film
        WHERE release_year IS NOT NULL
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchone()
