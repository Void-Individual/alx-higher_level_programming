#!/usr/bin/python3
"""Module for a db script"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    """Function to connect to mysql server"""

    db = MySQLdb.connect(host='localhost',
        user=username, passwd=password,
        db=db_name, port=3306)

    """Create a cursor object"""
    cursor = db.cursor()

    """Execute SQL query to retrieve states"""
    cursor.execute("SELECT * FROM states ORDER BY id")

    """Fetch all the displayed rows"""
    states = cursor.fetchall()

    """Display the fetched results"""
    for state in states:
        print(state)

    """Close cursor and end connection"""
    cursor.close()
    db.close

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    list_states(username, password, db_name)
