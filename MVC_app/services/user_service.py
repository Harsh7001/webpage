import json

from flask import request
#from models.machine import SamplePop,Populations,GeneticData,SNP,ClusteringAnalysis,Admixture, db

# Import necessary libraries
import sqlite3
import matplotlib
import os

import numpy as np
from sklearn.decomposition import PCA
matplotlib.use('agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
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

    pca_data = np.array(results)
    pca = PCA(n_components=2)

    pca_transformed = pca.fit_transform(pca_data[:, 1:3].astype(float))
    print("PCA Transformed---->",pca_transformed)

    # Create a list of unique populations
    unique_populations = list(set([result[3] for result in results]))

    # Create a color map for each population
    color_map = plt.cm.get_cmap('tab10', len(unique_populations))

    plt.figure(figsize=(8, 6))

    # Iterate over the results and plot each population with a different color
    for i, result in enumerate(results):
        population = result[3]
        color = color_map(unique_populations.index(population))
        plt.scatter(pca_transformed[i, 0], pca_transformed[i, 1], c=color, alpha=0.5)

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Plot')
    plt.grid(True)

    # Iterate over the results and plot each population with a different color
    for i, result in enumerate(results):
        population = result[3]
        color = color_map(unique_populations.index(population))
        plt.scatter(pca_transformed[i, 0], pca_transformed[i, 1], c=color, alpha=0.5, label=population)

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Plot')
    plt.grid(True)

    # Create a legend for the unique populations
    legend_labels = [population for population in unique_populations]
    # Create a color map for the legend
    legend_color_map = plt.cm.get_cmap('tab10', len(unique_populations))
    # Create a legend with the correct colors
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=legend_color_map(i), markersize=8) for i in range(len(unique_populations))]
    plt.legend(legend_handles, legend_labels)



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
        conn = sqlite3.connect('population_data.db')
        cursor = conn.cursor()
        print("PRINTINGGGGGG---->",ad_selected_populations)
        print("INSIDE IF")
        sql_query = "SELECT ad.id, ad.P1, ad.P2, sp.population FROM admixture as ad JOIN sample_pop as sp ON ad.id = sp.Id WHERE sp.population IN (SELECT population_code FROM populations WHERE superpopulation_code IN ({}))".format(','.join('?' for _ in ad_selected_populations))
        cursor.execute(sql_query, ad_selected_populations)
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
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Retrieve allele and genotype frequencies from the database (replace with your SQL query)
    allele_genotype_query = "SELECT * FROM allele_genotype_frequencies"
    cursor.execute(allele_genotype_query)
    allele_genotype_results = cursor.fetchall()

    # Retrieve clinical relevance information from the database (replace with your SQL query)
    clinical_relevance_query = "SELECT * FROM clinical_relevance"
    cursor.execute(clinical_relevance_query)
    clinical_relevance_results = cursor.fetchall()

    # Close the database connection
    conn.close()



# def retrieve_data(selection_type, **kwargs):
#     conn = sqlite3.connect('population_data.db')
#     cursor = conn.cursor()
#     populations = request.form.getlist('population')
#     print("Selection Type:", selection_type)
#     print("Populations:", populations)
#     if selection_type == 'id_list':
#         snp_ids = request.form['id_input'].split(',')
#         print("SNP IDs:", snp_ids)
#         # Retrieve data based on SNP IDs and selected populations
#         # Implement your SQL query here
#     elif selection_type == 'genomic_region':
#         chromosome = request.form['chrom_input']
#         start = request.form['start_input']
#         end = request.form['end_input']
#         print("Chromosome:", chromosome)
#         print("Start:", start)
#         print("End:", end)
#         # Retrieve data based on genomic region and selected populations
#         # Implement your SQL query here
#     elif selection_type == 'gene_list':
#         gene_names = request.form['gene_input'].split(',')
#         print("Gene Names:", gene_names)
#         # Retrieve data based on gene names and selected populations
#         # Implement your SQL query here
#     # Handle the retrieval of data and pairwise population genetic differentiation matrix
#     # Implement your logic here
#     return ("data")

def retrieve_data(selection_type, id_input=None, chrom_input=None, start_input=None, end_input=None, gene_input=None, populations=None):
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()

    # Initialize variables to hold retrieved data
    snp_data = []
    allele_genotype_freqs = []
    clinical_relevance = []
    pairwise_matrix = None

    # Logic to retrieve data based on the user's selection
    if selection_type == 'id_list':
        # Query database based on SNP IDs
        pass  # Implement your query logic here

    elif selection_type == 'genomic_region':
        # Query database based on genomic region
        pass  # Implement your query logic here

    elif selection_type == 'gene_list':
        # Query database based on gene names
        pass  # Implement your query logic here

    # If multiple populations are selected, calculate pairwise population genetic differentiation
    if populations and len(populations) > 1:
        # Calculate pairwise population genetic differentiation
        pairwise_matrix = None  # Implement your calculation logic here

    # Return the retrieved data
    return snp_data, allele_genotype_freqs, clinical_relevance, pairwise_matrix


def get_genotype_frequency(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations, connection):
    """
    Retrieves genotypic frequencies for a selected population based on criteria such as SNP ID, gene name, or genomic coordinates.
 
    """
    value = ''
    genotype_query = ''
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()
    if len(populations) > 0 and (":" in selected_SNPid or ";" in selected_SNPid or selected_SNPid.startswith("rs")):
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"HOM_ALT_{pop}, HETRO_{pop}, HOM_REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)
        
        genotype_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, gf.{selected_columns}
        from variant_table as vt
        join genotype_freqs as gf on vt.pos = gf.pos
        where snp_Id  =  %(val)s
        """
        
        value = {'val': selected_SNPid}
        cursor.execute(genotype_query, value)

    elif len(populations)>0 and len(selected_gene)>0:
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"HOM_ALT_{pop}, HETRO_{pop}, HOM_REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)
        
        genotype_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, gf.{selected_columns}
        from variant_table as vt
        join genotype_freqs as gf on vt.pos = gf.pos
        where geneName  =  %(val)s
        """
        value = {'val': selected_gene}

    elif len(populations)>0 and len(selected_genomic_start) and len(selected_genomic_end)>0:
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"HOM_ALT_{pop}, HETRO_{pop}, HOM_REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)

        genotype_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, gf.{selected_columns}
        from variant_table as vt
        join genotype_freqs as gf on vt.pos = gf.pos
        where vt.pos BETWEEN %(start)s AND %(end)s;
        """
        value = {'start': selected_genomic_start, 'end': selected_genomic_end}

    else: 
        print('Allele frequency not provided')

    data= pd.read_sql_query(genotype_query, connection, params=value)
    results = cursor.fetchall()     

    # Close the database connection
    conn.close()

    for pop in populations:
            # Calculate frequencies from the genotypic counts given and replace existing columns
            hom_alt_freq = (data[f'HOM_ALT_{pop.lower()}'] / data[[f'HOM_ALT_{pop.lower()}', f'HET_{pop.lower()}', f'HOM_REF_{pop.lower()}']].sum(axis=1)) * 100
            het_freq = (data[f'HET_{pop.lower()}'] / data[[f'HOM_ALT_{pop.lower()}', f'HET_{pop.lower()}', f'HOM_REF_{pop.lower()}']].sum(axis=1)) * 100
            hom_ref_freq = (data[f'HOM_REF_{pop.lower()}'] / data[[f'HOM_ALT_{pop.lower()}', f'HET_{pop.lower()}', f'HOM_REF_{pop.lower()}']].sum(axis=1)) * 100

            # Update existing columns with new frequencies
            data[f'HOM_ALT_{pop.lower()}'] = hom_alt_freq
            data[f'HET_{pop.lower()}'] = het_freq
            data[f'HOM_REF_{pop.lower()}'] = hom_ref_freq

'''
            hom_alt_freq = (data[f'{pop.lower()}_hom_alt'] / data[[f'{pop.lower()}_hom_alt', f'{pop.lower()}_het', f'{pop.lower()}_hom_ref']].sum(axis=1)) * 100
            het_freq = (data[f'{pop.lower()}_het'] / data[[f'{pop.lower()}_hom_alt', f'{pop.lower()}_het', f'{pop.lower()}_hom_ref']].sum(axis=1)) * 100
            hom_ref_freq = (data[f'{pop.lower()}_hom_ref'] / data[[f'{pop.lower()}_hom_alt', f'{pop.lower()}_het', f'{pop.lower()}_hom_ref']].sum(axis=1)) * 100
'''
def get_allele_frequency(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations, connection):
    """
    Retrieves allele frequencies for a selected population based on criteria such as SNP ID, gene name, or genomic coordinates.
 
    """
    value1 = ''
    allele_query = ''
    
    if len(populations) > 0 and (":" in selected_SNPid or ";" in selected_SNPid or selected_SNPid.startswith("rs")):
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"ALT_{pop}, REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)
        
        allele_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, af.{selected_columns}
        from variant_table as vt
        join allele_freqs as af on vt.pos = af.pos
        where snp_Id  =  %(val)s
        """
        value1 = {'val': selected_SNPid}

    elif len(populations)>0 and len(selected_gene)>0:
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"ALT_{pop}, REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)
        
        allele_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, af.{selected_columns}
        from variant_table as vt
        join allele_freqs as af on vt.pos = af.pos
        WHERE geneName = %(val)s
        """
        value1 = {'val': selected_gene}

    elif len(populations)>0 and len(selected_genomic_start) and len(selected_genomic_end)>0:
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"ALT_{pop}, REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)

        allele_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, af.{selected_columns}
        from variant_table as vt
        join allele_freqs as af on vt.pos = af.pos
        WHERE pos BETWEEN %(start)s AND %(end)s;
        """
        value1 = {'start': selected_genomic_start, 'end': selected_genomic_end}

    else: 
        print('Allele frequency not provided')

    data2= pd.read_sql_query(allele_query, connection, params=value1)


def get_clinical_relevance(selected_SNPid, selected_gene, selected_genomic_start, selected_genomic_end, populations, connection):
    """
    Retrieves clinical relevance for a selected population based on criteria such as SNP ID, gene name, or genomic coordinates.
 
    """
    value3 = ''
    genotype_query = ''
    
    if len(populations) > 0 and (":" in selected_SNPid or ";" in selected_SNPid or selected_SNPid.startswith("rs")):
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"HOM_ALT_{pop}, HETRO_{pop}, HOM_REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)
        
        genotype_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, gf.{selected_columns}
        from variant_table as vt
        join genotype_freqs as gf on vt.pos = gf.pos
        where snp_Id  =  %(val)s
        """
        
        value3 = {'val': selected_SNPid}

    elif len(populations)>0 and len(selected_gene)>0:
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"HOM_ALT_{pop}, HETRO_{pop}, HOM_REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)
        
        genotype_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, gf.{selected_columns}
        from variant_table as vt
        join genotype_freqs as gf on vt.pos = gf.pos
        where geneName  =  %(val)s
        """
        value3 = {'val': selected_gene}

    elif len(populations)>0 and len(selected_genomic_start) and len(selected_genomic_end)>0:
        # Assuming the column names follow the pattern: population_hom_ref, population_hom_alt and population_het
        population_columns = [f"HOM_ALT_{pop}, HETRO_{pop}, HOM_REF_{pop}" for pop in populations]
        selected_columns = ", ".join(population_columns)

        genotype_query= f"""
        select vt.pos,vt. geneName,vt. snp_Id,vt. ref, vt.alt, gf.{selected_columns}
        from variant_table as vt
        join genotype_freqs as gf on vt.pos = gf.pos
        where vt.pos BETWEEN %(start)s AND %(end)s;
        """
        value3 = {'start': selected_genomic_start, 'end': selected_genomic_end}

    else: 
        print('Allele frequency not provided')

    data= pd.read_sql_query(genotype_query, connection, params=valu)