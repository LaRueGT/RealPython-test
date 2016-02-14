# 6.6.2 assignment car orders

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""
        CREATE TABLE orders
        (make TEXT, model TEXT order_date TEXT)
        """)
    orders = [
        ('Honda', 'Civic', '2016-02-14'),
        ('Honda', 'Civic', '2016-02-14'),
        ('Honda', 'Civic', '2016-02-14'),
        ('Honda', 'Accord', '2016-02-14'),
        ('Honda', 'Accord', '2016-02-14'),
        ('Honda', 'Accord', '2016-02-14'),
        ('Honda', 'S2000', '2016-02-14'),
        ('Honda', 'S2000', '2016-02-14'),
        ('Honda', 'S2000', '2016-02-14'),
        ('Ford', 'Mustang', '2016-02-13'),
        ('Ford', 'Mustang', '2016-02-13'),
        ('Ford', 'Mustang', '2016-02-13'),
        ('Ford', 'F150', '2016-02-13'),
        ('Ford', 'F150', '2016-02-13'),
        ('Ford', 'F150', '2016-02-13')
     ]

    c.execute("SELECT * FROM orders")
    records = c.fetchall()