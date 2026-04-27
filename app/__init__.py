from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

storage = Redis(host="redis", port=6379, decode_responses=True)


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=os.getenv("STORAGE_URL")
)


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
    limiter.init_app(app)

    # Register blueprints
    from app.blueprints.home import home_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.files import files_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(files_bp)

    return app
