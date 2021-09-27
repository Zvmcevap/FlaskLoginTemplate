from . import db
from datetime import datetime
from flask_login import UserMixin


# Python classes to create Database tables with Flask-SQLAlchemy
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime)
    email = db.Column(db.String(100), unique=True)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'User: id:{self.id} name:{self.name} email:{self.email} registered{self.created_at}'
