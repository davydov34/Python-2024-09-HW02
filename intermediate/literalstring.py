from typing import LiteralString, Iterable


def intermediate_literalstring(sql: LiteralString, parameters: Iterable[str] = ...):
    pass


def query_user(user_id: str):
    query = f"SELECT * FROM data WHERE user_id = {user_id}"
    intermediate_literalstring(query)


def query_data(user_id: str, limit: bool) -> None:
    query = """
        SELECT
            user.name,
            user.age,
        FROM data
        WHERE user_id = ?
    """

    if limit:
        query += " LIMIT 1"

    intermediate_literalstring(query, (user_id,))
