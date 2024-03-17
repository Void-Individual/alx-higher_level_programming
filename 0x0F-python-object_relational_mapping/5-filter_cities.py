#!/usr/bin/python3
"""Module to run sql script"""

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
    query = "SELECT cities.name FROM cities INNER JOIN states ON\
        cities.state_id = states.id WHERE states.name = %s"

    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    city_names = ', '.join(city[0] for city in cities)
    print(city_names)
