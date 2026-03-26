from app.models import User
from app import db
import uuid
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime, timedelta


class AuthService:

    @staticmethod
    def user_payload(user):
        return {
            "id": str(user.id),
            "username": user.name,
            "email": user.email
        }

    @staticmethod
    def register(data):
        required_fields = ["username", "email", "password:", "confirm_password"]
        
        for field in required_fields:
            if field not in data:
                return {
                    "message": f"{field} is required"
                }, 400


        if data["password"] != data["confirm_password"]:
            return {
                "message": "Password do not match."
            }, 400

        if User.query.filter((User.email == data["email"]) | (User.username == data["username"])).first():
            return {
                "message": "User already exists"
            }, 400

        new_user = User(
            username=data["username"],
            email=data["email"]
        )
        new_user.set_password(data["password"])

        # save to db
        db.session.add(new_user)
        db.session.commit()

        return {
            "message": "User registered successfully"
        }, 201


    @staticmethod
    def login(data):
        user = User.query.filter_by(email=data["email"]).first()
        if not user or not user.check_password(data["password"]):
            return {
                "message": "Invalid credentials"
            }, 401

        access = create_access_token(identity=str(user.id))
        refresh = create_refresh_token(identity=str(user.id))

        return {
            "user": AuthService.user_payload(user),
            "tokens": {
                "access": access,
                "refresh": refresh
            }
        }, 200


    @staticmethod
    def refresh(identity):
        user = User.query.get(identity)
        access = create_access_token(identity=str(user.id))
        return {
            "access": access
        }, 200


    @staticmethod
    def logout():
        return {
            "message": "logged out successfully"
        }, 200


    @staticmethod

