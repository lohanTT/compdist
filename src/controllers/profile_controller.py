from log import log
from app import app
from auth import auth
from models.profile import Profile

# Routes
@app.route('/')
@auth.login_required
def index():
    user = auth.current_user()

    # Check if the user exist
    user_db = Profile.query.filter(Profile.username == user)

    # Avoid error while checking the users in database
    user_list = False
    try:
        user_list = user_db.all()[0]
    except IndexError:
        pass

    if user_list:
        message_info = f"Usuário {user}, acessou o index."

        response = {"success": message_info}
        log.info(message_info)

        return jsonify(response)
