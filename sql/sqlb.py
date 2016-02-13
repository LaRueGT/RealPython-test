# INSERT COMMAND with Error Handler

# import the sqlite3 library
import sqlite3

# create the connection object
with sqlite3.connect("new.db") as connection:

    # get a cursor object used to execute sql commands
    cursor = connection.cursor()

    try:
        # insert data
        cursor.execute("INSERT INTO populations  VALUES('New York City', \
                        'NY', 8200000)")
        cursor.execute("INSERT INTO populations VALUES('San Francisco', \
                        'CA', 800000)")
    except sqlite3.OperationalError:
        print("something went wrong, crap")


# unnecessary when using with..as clause
# commit changes
# conn.commit()
#
# close the database connection
# conn.close()

