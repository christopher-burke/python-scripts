#!/usr/bin/env python3

"""SQLite3 database creation."""

import sys
import sqlite3
from contextlib import contextmanager


@contextmanager
def create_db(name='db'):
    """Create database and yield cursor using contextmanager."""
    try:
        conn = sqlite3.connect(f'{name}.db')
        cursor = conn.cursor()
        yield cursor

    finally:
        conn.close()


if __name__ == "__main__":
    name = sys.argv[1]
    with create_db(name) as db:
        db.execute("""CREATE TABLE SAMPLE (first_name TEXT,
                                           last_name TEXT,
                                           dob INT)""")
