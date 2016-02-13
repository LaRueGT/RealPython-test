# 6.5 Homework

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    newinventory = [
        ('Honda', 'Civic', 5),
        ('Honda', 'Accord', 2),
        ('Honda', 'S2000', 1),
        ('Ford', 'F150', 3),
        ('Ford', 'Mustang', 7)
        ]
    c.executemany('INSERT INTO inventory VALUES (?, ?, ?)', newinventory)

    c.execute("UPDATE inventory SET quantity=3 WHERE model='Civic'")
    c.execute("UPDATE inventory SET quantity=4 WHERE model='F150' AND make='Ford'")

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    for record in rows:
        print(record[0], record[1], record[2])

    fords = c.execute("SELECT * FROM inventory WHERE make='Ford'")
    for row in fords:
        print(row)
