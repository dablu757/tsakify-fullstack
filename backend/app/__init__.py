from flask import Flask
from flask_jwt_extended import JWTManager
# from flask_sqlalchemy import SQLAlchemy
from app.config import DevConfig
from app.routes.auth import auth_bp
from app.models import db

jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    #initialize db and jwt instance into flask app
    db.init_app(app)
    jwt.init_app(app)

    #creating table
    from app.models import User, UserCredentials
    with app.app_context():
        db.create_all()

    #register app
    app.register_blueprint(auth_bp, url_prefix = '/auth')

    return app