import os

# secret key which used to sign session cookies for protection against cookie data tampering.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname('/Users/aditisahu/Documents/webpage/MVC_app'))

# Enable debug mode, that will refresh the page when you make changes.
DEBUG = True

# Connect to the MySQL database
SQLALCHEMY_DATABASE_URI = 'mysql://mysqluser:Gentoo123@localhost/population_data.db'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
