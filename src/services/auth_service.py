from auth import auth
from models.profile import Profile
from werkzeug.security import generate_password_hash, check_password_hash

@auth.verify_password
def verify_password(username, password):
    user = Profile.query.filter(Profile.username == username)

    if user.all():
        user_query = user.all()[0]
        if check_password_hash(generate_password_hash(user_query.password), password):
            return username


# Protect the Flask-Admin using username/password strings and SQLAlchemy
def validate_authentication(username, password):
    user = Profile.query.filter(Profile.username == username)

    if user.all():
        user_query = user.all()[0]
        if user_query.password == password:
            return True
        return False
    return False