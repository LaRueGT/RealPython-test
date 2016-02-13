# INSERT COMMAND

# import the sqlite3 library
import sqlite3

# create the connection object
with sqlite3.connect("new.db") as connection

# get a cursor object used to execute sql commands
cursor = connection.cursor()

# insert data
cursor.execute("INSERT INTO population  VALUES('New York City', \
                'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
                'CA', 800000)")

# unnecessary when using with..as clause
# commit changes
#conn.commit()
#
# close the database connection
#conn.close()

