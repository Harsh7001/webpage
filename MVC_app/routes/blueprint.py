from flask import Blueprint, render_template, request
from controllers.machineController import index, create, insert, clustering_analysis

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)

#blueprint.route('/clustering_analysis', methods=['GET'])(Clustering_analysis)

blueprint.route('/clustering_analysis', methods=['GET', 'POST'])(clustering_analysis)
