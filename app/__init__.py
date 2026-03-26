from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os


db = SQLAlchemy()


def create_app(config_object=Config):
    app = Flask(__name__)

    app.config.from_object(config_object)

    db.init_app(app)

    # Register blueprints
    from app.blueprints.home import home_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    return app
