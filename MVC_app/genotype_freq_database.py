
import csv
import sqlite3

# Define database name and table name
db_name = "population_data.db"
table_name = "genotype_freqs"

# Connect to the database
conn = sqlite3.connect(db_name)

# Open the TSV file in read mode
with open("genotype_freqs.tsv", "r") as f:
    # Create a CSV reader object
    reader = csv.reader(f, delimiter="\t")

    # Skip the header row (if present)
    next(reader)

    # Prepare the INSERT INTO statement
    insert_stmt = f"""INSERT INTO {table_name} (POS,
                    ID,
                    HOM_ALT_ACB ,
                    HETRO_ACB ,
                    HOM_REF_ACB ,
                    HOM_ALT_ASW ,
                    HETRO_ASW ,
                    HOM_REF_ASW ,
                    HOM_ALT_BEB ,
                    HETRO_BEB ,
                    HOM_REF_BEB ,
                    HOM_ALT_CDX ,
                    HETRO_CDX ,
                    HOM_REF_CDX ,
                    HOM_ALT_CHB ,
                    HETRO_CHB ,
                    HOM_REF_CHB ,
                    HOM_ALT_CHS ,
                    HETRO_CHS ,
                    HOM_REF_CHS ,
                    HOM_ALT_CLM ,
                    HETRO_CLM ,
                    HOM_REF_CLM ,
                    HOM_ALT_ESN ,
                    HETRO_ESN ,
                    HOM_REF_ESN ,
                    HOM_ALT_FIN ,
                    HETRO_FIN ,
                    HOM_REF_FIN ,
                    HOM_ALT_GIH ,
                    HETRO_GIH ,
                    HOM_REF_GIH ,
                    HOM_ALT_GRB ,
                    HETRO_GRB ,
                    HOM_REF_GRB ,
                    HOM_ALT_GWD ,
                    HETRO_GWD ,
                    HOM_REF_GWD ,
                    HOM_ALT_IBS ,
                    HETRO_IBS ,
                    HOM_REF_IBS ,
                    HOM_ALT_ITU ,
                    HETRO_ITU ,
                    HOM_REF_ITU ,
                    HOM_ALT_JPT ,
                    HETRO_JPT ,
                    HOM_REF_JPT ,
                    HOM_ALT_KHV ,
                    HETRO_KHV ,
                    HOM_REF_KHV ,
                    HOM_ALT_LWK ,
                    HETRO_LWK ,
                    HOM_REF_LWK ,
                    HOM_ALT_MSL ,
                    HETRO_MSL ,
                    HOM_REF_MSL ,
                    HOM_ALT_MXL ,
                    HETRO_MXL ,
                    HOM_REF_MXL ,
                    HOM_ALT_PEL ,
                    HETRO_PEL ,
                    HOM_REF_PEL ,
                    HOM_ALT_PJL ,
                    HETRO_PJL ,
                    HOM_REF_PJL ,
                    HOM_ALT_PUR ,
                    HETRO_PUR ,
                    HOM_REF_PUR ,
                    HOM_ALT_SIB ,
                    HETRO_SIB ,
                    HOM_REF_SIB ,
                    HOM_ALT_STU ,
                    HETRO_STU ,
                    HOM_REF_STU ,
                    HOM_ALT_TSI ,
                    HETRO_TSI ,
                    HOM_REF_TSI ,
                    HOM_ALT_YRI ,
                    HETRO_YRI ,
                    HOM_REF_YRI ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    # Iterate over the data and insert each row into the database
    for row in reader:
        conn.execute(insert_stmt, row)

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"Data from genotype_freqs.tsv successfully added to {table_name} in {db_name}")
