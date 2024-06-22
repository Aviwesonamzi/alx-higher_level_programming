#!/usr/bin/env python3
import MySQLdb
import sys

def list_cities(mysql_username, mysql_password, db_name):
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

    # Execute the SQL query to fetch all cities with their corresponding state names, sorted by city id
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all the results
    cities = cursor.fetchall()

    # Print each city
    for city in cities:
        print(city)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Extract arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # List the cities
    list_cities(mysql_username, mysql_password, db_name)
