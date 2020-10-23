import flask
from config import Config
from flask_mongoengine import MongoEngine
app=flask.Flask(__name__)
app.config.from_object(Config)
db=MongoEngine()
db.init_app(app)
from app import routes