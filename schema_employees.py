import sqlite3


def create_table(dbname='employees.db'):
    with sqlite3.connect(dbname) as connection:
        cur = connection.cursor()
        SQL = """DROP TABLE IF EXISTS names;"""

        cur.execute(SQL)

        SQL = """CREATE TABLE names(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            cellphone VARCHAR,
            homephone VARCHAR,
            workphone VARCHAR,
            email VARCHAR,
            country VARCHAR
            );"""

        cur.execute(SQL)


create_table()