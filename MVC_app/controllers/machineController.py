import json
import sqlite3
import matplotlib.pyplot as plt
from flask import render_template, request
from services.user_service import perform_clustering_analysis, perform_admixture_analysis, get_genotype_frequency, get_allele_frequency, get_clinical_relevance, get_ppdm_data


def index():
    return render_template('index.html')


def clustering_analysis():
    if request.method == 'POST':
        selected_populations = request.form.getlist('selected_populations')        
        
        clustering_results = perform_clustering_analysis(selected_populations)
        
        # rendering a template with the clustering results, or do any other processing
        return render_template('clustering_results.html', results=clustering_results)
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('clustering_analysis.html')
def admixture_analysis():
    if request.method == 'POST':
        ad_selected_populations = request.form.getlist('ad_selected_populations')
        # Now I have the selected populations in the list 'selected_populations'
    
        
        # Example:
        admixture_results = perform_admixture_analysis(ad_selected_populations)
        
        # rendering a template with the clustering results, or do any other processing
        
        return render_template('admixture_results.html', results=admixture_results)
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('admixture_analysis.html')





def genetic_information():
    return render_template('genetic_information.html')

def analyze():
    # getting the form submitted data
    selected_SNPid = request.form.get('selected_SNPid')
    selected_gene = request.form.get('selected_gene')
    selected_genomic_start = request.form.get('selected_genomic_start')
    selected_genomic_end = request.form.get('selected_genomic_end')
    populations = request.form.getlist('populations')

    print("selected_SNPid: ", selected_SNPid)
    print("populations: ", populations)

    genotype_data = get_genotype_frequency(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations)
    allele_data = get_allele_frequency(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations)
    clinical_data = get_clinical_relevance(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations)
    ppdm_data = get_ppdm_data(populations)
    # Joining the four datasets for testing purposes
    final_result = {
        'genotype_frequency': genotype_data,
        'allele_frequency': allele_data,
        'clinical_relevance': clinical_data,
        'pairwise_population_data': ppdm_data
    }
    print("controller_results: ", final_result)
    # Returning the processed data to results.html
    return render_template('results.html', genotype_data=genotype_data, allele_data=allele_data, clinical_data=clinical_data, ppdm_data=ppdm_data)

def about():
    if request.method == 'POST':
        return render_template('about.html')
    
    # If the request method is GET (initial loading of the page), simply render the form
    return render_template('about.html')

