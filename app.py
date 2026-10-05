import sqlite3
import subprocess


def get_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def ping(host):
    return subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True).returncode == 0
