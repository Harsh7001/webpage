import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('population_data.db')
cursor = conn.cursor()

# Create sample_id_table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS sample_id_table (
                    id TEXT,
                    population TEXT,
                    superpopulation_code TEXT
                )''')

# Read data from CSV and insert into the table
with open('sample_id.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Check if all keys are present in the row
        if 'id' in row and 'population' in row and 'superpopulation_code' in row:
            # Insert each row into the table
            cursor.execute('''INSERT INTO sample_id_table (id, population, superpopulation_code)
                              VALUES (?, ?, ?)''',
                           (row['id'], row['population'], row['superpopulation_code']))
        else:
            print("Skipping row:", row)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully into sample_id_table.")
