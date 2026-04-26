from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.blueprints.files.service import FileService
from flask import request, jsonify
from app import limiter

file_service = FileService()


class FileListUploadResource(Resource):
    decorators = [limiter.limit("10 per minute")]
    
    @jwt_required()
    def post(self):
        file = request.files.get("file")

        if not file:
            return jsonify({
                "error": "No file provided"
            }), 400

        user_id = get_jwt_identity()

        saved_file = file_service.upload_file(file, user_id)

        return jsonify({
            "id": saved_file.id,
            "filename": saved_file.filename
        })


    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        files = file_service.get_user_files(user_id)

        return jsonify([
            {
                "id": f.id,
                "filename": f.filename
            } for f in files
        ]) 



class FileDownloadResource(Resource):
    decorators = [limiter.limit("5 per minute")]
    
    @jwt_required()
    def get(self, file_id):
        user_id = get_jwt_identity()

        url = file_service.get_download_url(file_id, user_id)

        return {
            "url": url
        }, 200


class FileDeleteResource(Resource):
    decorators = [limiter.limit("5 per minute")]
    
    @jwt_required()
    def delete(self, file_id):
        user_id = get_jwt_identity()

        file_service.delete_file(file_id, user_id)

        return {
            "message": "Deleted"
        }, 200

