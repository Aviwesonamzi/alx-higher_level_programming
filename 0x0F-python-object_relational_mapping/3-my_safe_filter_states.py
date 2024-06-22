#!/usr/bin/env python3
import MySQLdb
import sys

def filter_states_by_name_safe(mysql_username, mysql_password, db_name, state_name):
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

    # Execute the SQL query to fetch states with the specified name, sorted by id
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

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
    state_name = sys.argv[4]

    # List the states with the specified name
    filter_states_by_name_safe(mysql_username, mysql_password, db_name, state_name)
