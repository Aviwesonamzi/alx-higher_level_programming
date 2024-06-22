#!/usr/bin/env python3
import MySQLdb
import sys

def list_cities_by_state(mysql_username, mysql_password, db_name, state_name):
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

    # Execute the SQL query to fetch all cities of the given state, sorted by city id
    query = """
    SELECT cities.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    WHERE states.name = %s 
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Print the cities as a comma-separated list
    print(", ".join([city[0] for city in cities]))

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Extract arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # List the cities of the specified state
    list_cities_by_state(mysql_username, mysql_password, db_name, state_name)
