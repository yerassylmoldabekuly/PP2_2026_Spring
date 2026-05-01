import psycopg2
from config import DB_CONFIG


def connect_db():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


def get_or_create_player(username):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    row = cur.fetchone()

    if row:
        player_id = row[0]
    else:
        cur.execute(
            "INSERT INTO players(username) VALUES (%s) RETURNING id",
            (username,)
        )
        player_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return player_id


def save_game_result(username, score, level_reached):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    row = cur.fetchone()

    if row:
        player_id = row[0]
    else:
        cur.execute(
            "INSERT INTO players(username) VALUES (%s) RETURNING id",
            (username,)
        )
        player_id = cur.fetchone()[0]

    cur.execute(
        """
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES (%s, %s, %s)
        """,
        (player_id, score, level_reached)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_top_scores(limit=10):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC, g.level_reached DESC, g.played_at ASC
        LIMIT %s
        """,
        (limit,)
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows


def get_personal_best(username):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT MAX(g.score)
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username = %s
        """,
        (username,)
    )
    row = cur.fetchone()

    cur.close()
    conn.close()
    return row[0] if row and row[0] is not None else 0