import json

from flask import request
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
    if 'EUR' in selected_populations or 'AMR' in selected_populations or 'SAS' in selected_populations or 'EAS' in selected_populations or 'AFR' in selected_populations or 'SIB' in selected_populations :       
    # Code for EUR population
        conn = sqlite3.connect('population_data.db')
        cursor = conn.cursor()
        print("PRINTINGGGGGG---->",selected_populations)
        print("INSIDE IF")
        sql_query = "SELECT pc.SampleID, pc.PCA_1, pc.PCA_2, sp.population FROM pca_table as pc JOIN sample_pop as sp ON pc.SampleId = sp.Id WHERE sp.population IN (SELECT population_code FROM populations WHERE superpopulation_code IN ({}))".format(','.join('?' for _ in selected_populations))
        cursor.execute(sql_query, selected_populations)
    else:
        conn = sqlite3.connect('population_data.db')
        cursor = conn.cursor()
        print("PRINTINGGGGGG---->",selected_populations)
        print("INSIDE ELSE")
        # Retrieve PCA results from the database
        sql_query= "SELECT pc.SampleID, pc.PCA_1, pc.PCA_2, sp.population FROM pca_table as pc JOIN sample_pop as sp ON pc.SampleId = sp.Id WHERE sp.population IN ({})".format(','.join('?' for _ in selected_populations))
        cursor.execute(sql_query, selected_populations)
    results = cursor.fetchall()     

    # Close the database connection
    conn.close()
    print("RESULTS---->",results)
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

# Implement the admixture analysis function

def perform_admixture_analysis(ad_selected_populations):
    print("Selected populations:", ad_selected_populations)
    if 'EUR' in ad_selected_populations or 'AMR' in ad_selected_populations or 'SAS' in ad_selected_populations or 'EAS' in ad_selected_populations or 'AFR' in ad_selected_populations or 'SIB' in ad_selected_populations :       
    # Code for EUR population
        conn = sqlite3.connect('population_data.db')
        cursor = conn.cursor()
        print("PRINTINGGGGGG---->",ad_selected_populations)
        print("INSIDE IF")
        sql_query = "SELECT ad.id, ad.P1, ad.P2, sp.population FROM admixture as ad JOIN sample_pop as sp ON ad.id = sp.Id WHERE sp.population IN (SELECT population_code FROM populations WHERE superpopulation_code IN ({}))".format(','.join('?' for _ in ad_selected_populations))
        cursor.execute(sql_query, ad_selected_populations)
# Import necessary libraries
    else:
        conn = sqlite3.connect('population_data.db')
        cursor = conn.cursor()
        print("PRINTINGGGGGG---->",ad_selected_populations)
        print("INSIDE ELSE")
        # Retrieve PCA results from the database
        sql_query= "SELECT ad.id, ad.P1, ad.P2, sp.population FROM admixture as ad JOIN sample_pop as sp ON ad.id = sp.Id WHERE sp.population IN ({})".format(','.join('?' for _ in ad_selected_populations))
        cursor.execute(sql_query, ad_selected_populations)
    # Connect to the database

    results = cursor.fetchall()     

    # Close the database connection
    conn.close()

    # Extract PC1, PC2, and SampleID values
    sample_ids = [result[0] for result in results]
    p1_values = [result[1] for result in results]
    p2_values = [result[2] for result in results]

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(p1_values, p2_values, c='steelblue', alpha=0.5)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Admixture Plot')
    plt.grid(True)

    # Annotate sample IDs on the plot
    for i, sample_id in enumerate(sample_ids):
        plt.annotate(sample_id, (p1_values[i], p2_values[i]))

    # Save the plot as an image file
    adplot_filepath = '/Users/aditisahu/Documents/webpage/MVC_app/static/Admixture_plot.png'
    plt.savefig(adplot_filepath)

    # Clear the plot
    plt.clf()

    # Implement clustering analysis logic here based on the selected populations
    # This function should return the clustering results
    # Example: clustering_results = clustering_algorithm(selected_populations)
    admixture_results = "Admixture results for selected populations: {}".format(ad_selected_populations)
    
    return admixture_results, adplot_filepath

def process_genetic_info():
    return "Genetic information processed successfully."
        # Here you can perform further processing of the data,
        # such as database operations or analysis.
