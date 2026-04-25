from flask import Blueprint
from app.blueprints.files.routes import register_routes

files_bp = Blueprint("files", __name__, url_prefix="/api/files")

register_routes(files_bp)
