import flask
from config import Config
from flask_mongoengine import MongoEngine
app=flask.Flask(__name__)
from app import routes