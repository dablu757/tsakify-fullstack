from flask import Flask
from flask_jwt_extended import jwt_manager
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()
jwt = jwt_manager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    #initialize db and jwt instance into flask app
    db.init_app(app)
    db.init_app(jwt)

    return app