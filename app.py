import sqlite3
import subprocess

"""Small helpers for the playground."""

def get_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def ping(host):
    return subprocess.run(["ping", "-c", "1", host], capture_output=True).returncode == 0
