#!/usr/bin/python3
"""Module for a sql script"""

import sys
import MySQLdb


def filter_states(username, password, db_name):
    """Function to connect to a sql server"""

    db = MySQLdb.connect(
        host='localhost',
        user=username, passwd=password,
        db=db_name, port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states where name LIKE 'N%' ORDER BY id")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    filter_states(username, password, db_name)
