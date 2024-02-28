import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('population_data.db')
cursor = conn.cursor()

# Create variant_table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS variant_table (
                    id TEXT,
                    population_code INTEGER,
                    superpopulation_code TEXT,
                )''')

# Read data from CSV and insert into the table
with open('variant_table.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert each row into the table
        cursor.execute('''INSERT INTO variant_table (id, population_code, superpopulation_code)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (row['id'], int(row['population']), row['snp_id'], row['ref'], row['alt'], row['geneName']))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully into variant_table.")
