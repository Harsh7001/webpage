import json
import sqlite3
import matplotlib.pyplot as plt
from flask import render_template, request
# from models.machine import SamplePop,Populations,GeneticData,SNP,ClusteringAnalysis,Admixture, db
from services.user_service import perform_clustering_analysis


def index():
    return {'status': 'OK',
            'localhost:5000/create': 'Create table in mysql database',
            'localhost:5000/insert': 'Insert data in mysql database table(Inserttable)'}

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
        
        # You can pass this list to your clustering function for further processing
        
        # Example:
        clustering_results = perform_clustering_analysis(selected_populations)
        
        # You can then render a template with the clustering results, or do any other processing
        
        return render_template('clustering_results.html', results=clustering_results)
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('clustering_analysis.html')
