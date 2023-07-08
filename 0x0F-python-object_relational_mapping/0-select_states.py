#!/usr/bin/python3
"""
This script lists all staes from the database hbtn_0e_0_usa
:"""
import MySQLdb
import sys
"""
Import the MySQLdb and sys module
"""
username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    """
    A connection is established to the MySQL database
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        passwd=password,
        db=db_name
        )
    cursor = db.cursor()
    """
    Create the cursor object
    """
    cursor.execute("SELECT * FROM states")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
