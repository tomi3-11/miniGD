from flask import jsonify
from flask_restful import Resource
from app import limiter


class HomeResource(Resource):
    decorators = [limiter.limit("10 per minute")]
    
    def get(self):
        return jsonify({
            "message": "Welcome to my mini Google Drive",
            "Details": "This is simply an experiment building a mini google drive, the goal is to know how to work with files and object storage locally using minIO"
        }, 200)
