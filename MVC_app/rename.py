import sqlite3

# Connect to the database
conn = sqlite3.connect('population_data.db')
cursor = conn.cursor()

# Rename the columns in the pca_table
cursor.execute("ALTER TABLE ppdm_data RENAME COLUMN 'Unnamed:0' TO population")


# Commit the changes and close the connection
conn.commit()
conn.close()