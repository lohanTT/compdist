from models.profile import Profile
from config import config
from db import db


def isAdmin(username):
    admin = Profile.query.filter(Profile.username == username).first()

    if admin is None:
        return False
    
    return admin.isAdmin

def init_admin_profile():
    admin = Profile.query.filter(Profile.username == config.adminUser).first()
    if not admin:
        admin = Profile(username=config.adminUser, password=config.adminPassword, email=None, isAdmin=True)
        db.session.add(admin)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

