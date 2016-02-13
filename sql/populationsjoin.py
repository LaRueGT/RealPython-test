# JOINING data from multiple tables - cleaned up

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""
        SELECT DISTINCT population.city, population.population,
        regions.region FROM population, regions
        WHERE population.city = regions.city
        ORDER BY population.city ASC
        """)

    rows = c.fetchall()

    for r in rows:
        print("City: " + r[0], "Population: " + str(r[1]), "Region: " + r[2])
