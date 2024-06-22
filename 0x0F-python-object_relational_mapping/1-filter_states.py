#!/usr/bin/env python3
import MySQLdb
import sys

def list_states_with_n(mysql_username, mysql_password, db_name):
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch states with names starting with 'N', sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Extract arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # List the states with names starting with 'N'
    list_states_with_n(mysql_username, mysql_password, db_name)
