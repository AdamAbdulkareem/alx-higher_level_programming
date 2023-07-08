#!/usr/bin/python3
"""
This script lists all the states with a name starting with N
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

"""
Import MySQLdb and sys module
"""

if __name__ == "__main__":
    """
    A connection is established to the MySQL database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )
    cursor = db.cursor()
    """
    Create a cursor
    """
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_general_ci"
    )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
