from flask import Flask
from config import config

app = Flask("Comp dist")

# Configuration
app.config['FLASK_SECRET'] = config.secretKey
app.config['BASIC_AUTH_FORCE'] = True
app.secret_key = config.secretKey

# Set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

# Adding configuration for using a database
app.config['SQLALCHEMY_DATABASE_URI'] = config.database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False