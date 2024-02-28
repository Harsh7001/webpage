import json
import sqlite3
import matplotlib.pyplot as plt
from flask import render_template, request
# from models.machine import SamplePop,Populations,GeneticData,SNP,ClusteringAnalysis,Admixture, db
from services.user_service import perform_clustering_analysis, perform_admixture_analysis, process_genetic_info


def index():
    return render_template('index.html')

def create():   
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()

    # Handle POST request
    if request.method == 'POST':
        selected_population = request.form['position']
        cursor.execute("SELECT * FROM ID WHERE sample_pop = ?;", (selected_population,))
    else:
        # Default to showing all populations if no selection made
        cursor.execute("SELECT DISTINCT population FROM sample_pop;")
        populations = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT * FROM sample_pop;")
    
    rows = cursor.fetchall()
    conn.close()

    return render_template('index.html', rows=rows, populations=populations)

def insert():
    ("insert_logic")

def clustering_analysis():
    if request.method == 'POST':
        selected_populations = request.form.getlist('selected_populations')
        # Now you have the selected populations in the list 'selected_populations'
        superpopulations = request.form.getlist('superpopulations')
        # You can pass this list to your clustering function for further processing
        
        # Example:
        clustering_results = perform_clustering_analysis(selected_populations or superpopulations)
        
        # You can then render a template with the clustering results, or do any other processing
        
        return render_template('clustering_results.html', results=clustering_results)
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('clustering_analysis.html')
def admixture_analysis():
    if request.method == 'POST':
        selected_populations = request.form.getlist('selected_populations')
        # Now you have the selected populations in the list 'selected_populations'
        
        # You can pass this list to your clustering function for further processing
        
        # Example:
        admixture_results = perform_admixture_analysis(selected_populations)
        
        # You can then render a template with the clustering results, or do any other processing
        
        return render_template('admixture_results.html', results=admixture_results)
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('admixture_analysis.html')
def genetic_information():
    if request.method == 'POST':
       # Get form data
        snp_id = request.form['snp_id']
        gene_name = request.form['gene_name']
        start_position = request.form['start_position']
        end_position = request.form['end_position']
        selected_populations = request.form.getlist('selected_populations')

        # Process the form data (you can replace this with your logic)
        # For demonstration, let's just print the received data
        print("SNP ID:", snp_id)
        print("Gene Name:", gene_name)
        print("Start Position:", start_position)
        print("End Position:", end_position)
        print("Selected Populations:", selected_populations)

        return render_template('genetic_results.html')
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('genetic_information.html')
def about():
    if request.method == 'POST':
        return render_template('about.html')
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('about.html')


def retrieve_snp_info():
    # Get form data
    selection_type = request.form['selection_type']
    
    if selection_type == 'snp_id':
        snp_id = request.form['snp_id']
        # Query database or perform analysis based on SNP ID
        # Return relevant information to the user
    
    elif selection_type == 'genomic_coordinates':
        chromosome = request.form['chromosome']
        start_position = request.form['start_position']
        end_position = request.form['end_position']
        # Query database or perform analysis based on genomic coordinates
        # Return relevant information to the user
    
    elif selection_type == 'gene_names':
        gene_names = request.form.getlist('gene_names')
        # Query database or perform analysis based on gene names
        # Return relevant information to the user
    
    return "Sample allele and genotype frequencies, as well as clinical relevance information, retrieved successfully!"