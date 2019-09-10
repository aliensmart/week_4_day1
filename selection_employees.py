import sqlite3

#fetches all data WHERE country = Mongolia
#print all rows when that condition is TRUE

SQL = """SELECT * FROM names WHERE country='USA';"""

with sqlite3.connect('employees.db') as connection:
    cur = connection.cursor()
    cur.execute(SQL)
    data = cur.fetchall()
    print(data)

