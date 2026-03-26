from .routes import register_blueprint
from flask import Blueprint

home_bp = Blueprint("home", __name__)

register_blueprint(home_bp)
