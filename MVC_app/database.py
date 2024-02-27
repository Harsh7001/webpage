import sqlite3

try:
    conn_population = sqlite3.connect('population_data.db')
    conn_genotype = sqlite3.connect('genotype_frequencies.db')

    # Get cursors for both databases
    cursor_population = conn_population.cursor()
    cursor_genotype = conn_genotype.cursor()

    # Create a new table in population_data.db
    cursor_population.execute('''CREATE TABLE IF NOT EXISTS genotype_freq ( "POS" TEXT, "ID" TEXT, "HOM_ALT_ACB" TEXT, "HETRO_ACB" TEXT, "HOM_REF_ACB" TEXT, "HOM_ALT_ASW" TEXT, "HETRO_ASW" TEXT, "HOM_REF_ASW" TEXT, "HOM_ALT_BEB" TEXT, "HETRO_BEB" TEXT, "HOM_REF_BEB" TEXT, "HOM_ALT_CDX" TEXT, "HETRO_CDX" TEXT, "HOM_REF_CDX" TEXT, "HOM_ALT_CHB" TEXT, "HETRO_CHB" TEXT, "HOM_REF_CHB" TEXT, "HOM_ALT_CHS" TEXT, "HETRO_CHS" TEXT, "HOM_REF_CHS" TEXT, "HOM_ALT_CLM" TEXT, "HETRO_CLM" TEXT, "HOM_REF_CLM" TEXT, "HOM_ALT_ESN" TEXT, "HETRO_ESN" TEXT, "HOM_REF_ESN" TEXT, "HOM_ALT_FIN" TEXT, "HETRO_FIN" TEXT, "HOM_REF_FIN" TEXT, "HOM_ALT_GBR" TEXT, "HETRO_GBR" TEXT, "HOM_REF_GBR" TEXT, "HOM_ALT_GIH" TEXT, "HETRO_GIH" TEXT, "HOM_REF_GIH" TEXT, "HOM_ALT_GWD" TEXT, "HETRO_GWD" TEXT, "HOM_REF_GWD" TEXT, "HOM_ALT_IBS" TEXT, "HETRO_IBS" TEXT, "HOM_REF_IBS" TEXT, "HOM_ALT_ITU" TEXT, "HETRO_ITU" TEXT, "HOM_REF_ITU" TEXT, "HOM_ALT_JPT" TEXT, "HETRO_JPT" TEXT, "HOM_REF_JPT" TEXT, "HOM_ALT_KHV" TEXT, "HETRO_KHV" TEXT, "HOM_REF_KHV" TEXT, "HOM_ALT_LWK" TEXT, "HETRO_LWK" TEXT, "HOM_REF_LWK" TEXT, "HOM_ALT_MSL" TEXT, "HETRO_MSL" TEXT, "HOM_REF_MSL" TEXT, "HOM_ALT_MXL" TEXT, "HETRO_MXL" TEXT, "HOM_REF_MXL" TEXT, "HOM_ALT_PEL" TEXT, "HETRO_PEL" TEXT, "HOM_REF_PEL" TEXT, "HOM_ALT_PJL" TEXT, "HETRO_PJL" TEXT, "HOM_REF_PJL" TEXT, "HOM_ALT_PUR" TEXT, "HETRO_PUR" TEXT, "HOM_REF_PUR" TEXT, "HOM_ALT_SIB" TEXT, "HETRO_SIB" TEXT, "HOM_REF_SIB" TEXT, "HOM_ALT_STU" TEXT, "HETRO_STU" TEXT, "HOM_REF_STU" TEXT, "HOM_ALT_TSI" TEXT, "HETRO_TSI" TEXT, "HOM_REF_TSI" TEXT, "HOM_ALT_YRI" TEXT, "HETRO_YRI" TEXT, "HOM_REF_YRI" TEXT)''')

    # Fetch data from genotype_frequencies.db
    cursor_genotype.execute('SELECT * FROM my_table')
    data = cursor_genotype.fetchall()

    # Insert the fetched data into the newly created table in population_data.db
    cursor_population.executemany('INSERT INTO genotype_freq VALUES (?,?,...,?)', data)

    # Commit the changes and close the connections
    conn_population.commit()
    conn_genotype.commit()
    conn_population.close()
    conn_genotype.close()
except sqlite3.Error as e:
    print("An error occurred:", e)
