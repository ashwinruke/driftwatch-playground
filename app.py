import sqlite3
import subprocess

API_KEY = "sk-test-4f9a1c7e2b8d6f03a5e9"

def get_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def ping(host):
    return subprocess.run(["ping", "-c", "1", host], capture_output=True).returncode == 0
