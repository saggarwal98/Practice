from app import db
import flask
class User(db.Document):
    user_name=db.StringField(max_length=100)
    user_email=db.StringField(max_length=30)
    user_password=db.StringField(max_length=30)