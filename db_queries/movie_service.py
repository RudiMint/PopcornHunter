from utils.mysql_connection import get_connection

def movie_query(args):
    """
    Build a parameterized SQL query for searching movies.
    :param args: Search arguments object containing optional attributes:
                 ``tag``, ``genre``, and ``year_range``.
    :return: A tuple containing:
             - SQL query string with parameter placeholders.
             - List of parameters corresponding to the placeholders.
    """
    query = """
        SELECT
        f.film_id,
        f.title,
        f.release_year,
        f.description
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
    """
    Retrieve all movie genres from the database.
    :type conn: object
    :return: A list of genre names.
    """
    query = "SELECT name FROM category"

    with conn.cursor() as cursor:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]


def get_year_range(conn):
    """
    Retrieve the minimum and maximum release years available in the film catalog.
    :param conn:
    :return: A tuple containing the minimum and maximum release years
    """
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


def execute_query(query, params):
    """
    Execute a parameterized SQL query and return all resulting rows.
    :param query: SQL query string to execute. The query may contain
                  parameter placeholders supported by the database driver.
    :param params: Parameters to bind to the query placeholders. If
                   ``None`` or empty, the query is executed without
                   additional parameters.
    :return: All rows returned by the query.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params or [])
            return cursor.fetchall()

