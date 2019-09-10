import csv
import sqlite3

with open('employees.csv') as file_object:
    reader = csv.DictReader(file_object)
    for row in reader:
        #create a connection
        with sqlite3.connect('employees.db') as connection:
        #create a cursor
            cur = connection.cursor()
        #create a string
            SQL = """INSERT INTO names(
            name, cellphone, homephone, 
            workphone, email, country) 
            VALUES (?,?,?,?,?,?); """
            data = (row['name'], row['cellphone'], row['homephone'], 
            row['workphone'], row['email'], row['country'])
        #execute
            cur.execute(SQL, data)