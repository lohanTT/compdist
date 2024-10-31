from db import db
from config import config


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(65), unique=True, nullable=True)
    registered = db.Column(db.DateTime(timezone=True), default=db.func.now())
    isAdmin = db.Column(db.Boolean, default=False)

    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"{self.username} {self.email} {self.isAdmin}"
    