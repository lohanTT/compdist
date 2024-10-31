
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from auth import auth

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)