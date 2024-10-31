from app import app
import admin
import controllers.profile_controller
from db import db
from services.profile_service import init_admin_profile

# Initialize the application
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        init_admin_profile() 

    app.run(host="0.0.0.0", debug=True, port=8080)
