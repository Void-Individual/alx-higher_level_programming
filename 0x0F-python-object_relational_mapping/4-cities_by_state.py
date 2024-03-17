#!/usr/bin/python3
"""Module to run a sql script"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
