from log import log
from app import app
from auth import auth
import controllers.profile_controller
from models.profile import Profile
from db import db
from admin import admin
from services.auth_service import validate_authentication
from flask import jsonify
from flask_admin import Admin
from views.profile_view import ProfileView

# Initialize the application
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", debug=True, port=8080)
