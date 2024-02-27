import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="mysql_user",
    password="Gentoo123",
    database="population_data.db"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Execute a sample query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Process the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()