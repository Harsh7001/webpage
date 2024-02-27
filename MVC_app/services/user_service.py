import json
#from models.machine import SamplePop,Populations,GeneticData,SNP,ClusteringAnalysis,Admixture, db


"""""
def create_logic():
    try:
        # create tables if not exists.
        db.create_all()
        db.session.commit()
        return '==================TABLES CREATED=================='

    except Exception as e:
        print(e)
        return '==================TABLES NOT CREATED!!!=================='


def insert_logic():
    data = json.load(open("data.json", 'r'))  # reading file data.json
    for i, b in enumerate('{0:016b}'.format(data['StateId'])):
        if int(b) == 1:
            example = Inserttable(machineid=data["MachineId"], stateid=data["StateId"],
                                  speed=data["Speed"], statechange=data["StateChange"],
                                  unixtime=data["UnixTime"], extras=data["Extras"],
                                  state="ON")

            db.session.add(example)
            # db.session.commit()

        else:
            example = Inserttable(machineid=data["MachineId"], stateid=data["StateId"],
                                  speed=data["Speed"], statechange=data["StateChange"],
                                  unixtime=data["UnixTime"], extras=data["Extras"],
                                  state="OFF")

            db.session.add(example)
            # db.session.commit()
    return '==================DATA INSERTED=================='
    db.session.commit()
"""""
# Import necessary libraries
import sqlite3
import matplotlib
import os
matplotlib.use('agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
def perform_clustering_analysis(selected_populations):
    # Connect to the database
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()

    # Retrieve PCA results from the database
    
    cursor.execute('SELECT pc.SampleID, pc.PCA_1, pc.PCA_2, sp.population, sp.superpopulation_code FROM pca_table as pc JOIN sample_pop as sp ON pc.SampleId = sp.id WHERE sp.population_code IN (selected_populations)')
    results = cursor.fetchall()     

    # Close the database connection
    conn.close()

    # Extract PC1, PC2, and SampleID values
    sample_ids = [result[0] for result in results]
    pc1_values = [result[1] for result in results]
    pc2_values = [result[2] for result in results]

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(pc1_values, pc2_values, c='blue', alpha=0.5)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Plot')
    plt.grid(True)

    # Annotate sample IDs on the plot
    for i, sample_id in enumerate(sample_ids):
        plt.annotate(sample_id, (pc1_values[i], pc2_values[i]))

    # Save the plot as an image file
    plot_filepath = '/Users/aditisahu/Documents/webpage/MVC_app/static/PCA_plot.png'
    plt.savefig(plot_filepath)

    # Clear the plot
    plt.clf()

    # Implement clustering analysis logic here based on the selected populations
    # This function should return the clustering results
    # Example: clustering_results = clustering_algorithm(selected_populations)
    clustering_results = "Clustering results for selected populations: {}".format(selected_populations)
    
    return clustering_results, plot_filepath
