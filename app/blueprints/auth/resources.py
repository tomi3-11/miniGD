from flask_restful import Resource
from flask import jsonify, request
from .services import AuthService
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
import uuid


class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        result, status = AuthService.register(data)
        return jsonify(result, status)


class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        result, status = AuthService.login(data)
        return jsonify(result, status)


class LogoutResource(Resource):
    def post(self):
        data = AuthService.logout()
        return jsonify(data)
        

class TokenRefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        data = AuthService.refresh(identity)
        return jsonify(data)


class CurrentUserResource(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()

        try:
            user_uuid = uuid.UUID(identity)  
        except ValueError:
            return jsonify({
                "error": "Invalid user ID"
            }), 400

        user = User.query.get(user_uuid)

        if not user:
            return jsonify({
                "error": "User not found"
            }, 404)

        data = AuthService.user_payload(user)
        return jsonify(data, 200)


class PasswordResetRequestResource(Resource):
    def post(self):
        data = request.get_json()
        result, status = AuthService.reset_request_password(data)
        return (result, status)


class PasswordResetConfirmResource(Resource):
    def post(self):
        data = request.get_json()
        result, status = AuthService.reset_password(data)
        return jsonify(result, status)
    
