from flask import Flask

app = Flask("Comp dist")
# Configuration
app.config.from_pyfile('cfg/app.cfg', silent=True)
app.config['FLASK_SECRET'] = app.config.get('SECRET_KEY')
app.config['BASIC_AUTH_FORCE'] = True
app.secret_key = app.config.get('SECRET_KEY')

# Set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

# adding configuration for using a database
app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False