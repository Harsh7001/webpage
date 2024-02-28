from flask import Blueprint, render_template, request
from controllers.machineController import index, create, insert, clustering_analysis,admixture_analysis,genetic_information

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)

#blueprint.route('/clustering_analysis', methods=['GET'])(Clustering_analysis)

blueprint.route('/clustering_analysis', methods=['GET', 'POST'])(clustering_analysis)
blueprint.route('/admixture_analysis', methods=['GET', 'POST'])(admixture_analysis)
blueprint.route('/genetic_information', methods=['GET', 'POST'])(genetic_information)
blueprint.route('/about', methods=['GET', 'POST'])(clustering_analysis)
