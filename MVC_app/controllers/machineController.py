import json
import sqlite3
import matplotlib.pyplot as plt
from flask import render_template, request
# from models.machine import SamplePop,Populations,GeneticData,SNP,ClusteringAnalysis,Admixture, db
from services.user_service import perform_clustering_analysis, perform_admixture_analysis, get_genotype_frequency, get_allele_frequency, get_clinical_relevance


def index():
    return render_template('index.html')


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
def admixture_analysis():
    if request.method == 'POST':
        ad_selected_populations = request.form.getlist('ad_selected_populations')
        # Now you have the selected populations in the list 'selected_populations'
        
        # You can pass this list to your clustering function for further processing
        
        # Example:
        admixture_results = perform_admixture_analysis(ad_selected_populations)
        
        # You can then render a template with the clustering results, or do any other processing
        
        return render_template('admixture_results.html', results=admixture_results)
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('admixture_analysis.html')





def genetic_information():
    return render_template('genetic_information.html')

def analyze():
    selected_SNPid = request.form.get('selected_SNPid')
    selected_gene = request.form.get('selected_gene')
    selected_genomic_start = request.form.get('selected_genomic_start')
    selected_genomic_end = request.form.get('selected_genomic_end')
    populations = request.form.getlist('populations')

    print("selected_SNPid: ", selected_SNPid)
    print("populations: ", populations)

    data = get_genotype_frequency(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations)
    data1 = get_allele_frequency(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations)
    data2 = get_clinical_relevance(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations)
    # data3 = g
    # Join the three datasets
    final_result = {
        'genotype_frequency': data,
        'allele_frequency': data1,
        'clinical_relevance': data2
    }
    print("controller_results: ", final_result)
    # Process the final result as needed
    # Return the processed data to results.html
    return render_template('results.html', final_result=final_result)

def about():
    if request.method == 'POST':
        return render_template('about.html')
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('about.html')

