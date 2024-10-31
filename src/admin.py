from flask_admin import Admin
from views.profile_view import ProfileView
from models.profile import Profile
from app import app
from db import db

admin = Admin(app, name='Super App', template_mode='bootstrap4')
admin.add_view(ProfileView(Profile, db.session))