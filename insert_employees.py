import sqlite3

#script python that will let me add data to db, until I decide to stop

while True:
    name = input("name: ")
    if name == 'done':
        break
    cellphone = input("cellphone: ")
    homephone = input("homephone: ")
    workphone = input("workphone: ")
    email = input("email: ")
    country = input("country: ")

    with sqlite3.connect('employees.db') as connection:
        cur = connection.cursor()
        SQL = """INSERT INTO names(
                    name, cellphone, homephone, 
                    workphone, email, country)
                    VALUES (?,?,?,?,?,?);"""
        data = (name, cellphone, homephone, 
                    workphone, email, country)
        
        cur.execute(SQL, data)