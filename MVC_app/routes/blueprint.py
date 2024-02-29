from flask import Blueprint, render_template, request
from controllers.machineController import index, clustering_analysis,admixture_analysis,genetic_information,about, analyze

blueprint = Blueprint('blueprint', __name__)

#Adding blueprints which will route the request to the respective functions

blueprint.route('/', methods=['GET'])(index)

blueprint.route('/clustering_analysis', methods=['GET', 'POST'])(clustering_analysis)
blueprint.route('/admixture_analysis', methods=['GET', 'POST'])(admixture_analysis)
blueprint.route('/genetic_information', methods=['GET', 'POST'])(genetic_information)
blueprint.route('/analyze', methods=['POST'])(analyze)
blueprint.route('/about', methods=['GET'])(about)
