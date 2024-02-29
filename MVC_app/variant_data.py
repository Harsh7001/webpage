import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('population_data.db')

# Read the CSV file into a DataFrame
df = pd.read_csv('ppdm_transformed.csv')

# Write the DataFrame to a SQLite table
df.to_sql('ppdm_data', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
