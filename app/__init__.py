from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()


def create_app(config_object=None):
    app = Flask(__name__)

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(Config)
        

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from app.blueprints.home import home_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    return app
