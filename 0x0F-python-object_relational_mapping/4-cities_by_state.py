#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

"""
Import the MySQLdb and sys module
"""

if __name__ == "__main__":
    """
    A connection is established to the MySQL database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", user=username, port=3306, passwd=password, db=db_name
    )
    cursor = db.cursor()
    """
    Create the cursor object
    """
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id ORDER BY state_id ASC"
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
