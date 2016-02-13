# import sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute sql commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
                  (make TEXT, model TEXT, quantity INT)
                """)

# close the database connection
conn.close()
