from app.models import User
from app import db, mail
import uuid
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime, timedelta
from flask_mail import Message


class AuthService:

    @staticmethod
    def user_payload(user):
        return {
            "id": str(user.id),
            "username": user.username,
            "email": user.email
        }

    @staticmethod
    def register(data):
        required_fields = ["username", "email", "password", "confirm_password"]
        
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
        try:
            uuid_user = uuid.UUID(identity)
        except ValueError:
            return {
                "message": "Ivalid User Data"
            }, 400
        user = User.query.get(uuid_user)
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
    def request_reset_password(data):
        user = User.query.filter_by(email=data["email"]).first()
        if not user:
            return {
                "message": "User not found"
            }, 404

        token = str(uuid.uuid4())
        user.reset_token = token
        user.reset_token_expiry = datetime.utcnow() + timedelta(minutes=30)

        db.session.commit()

        # link to use for redirection
        url = f"http://localhost:5000/api/auth/reset_password?token={token}"

        msg = Message(
            subject="Password Reset",
            recipients=[user.email],
            body=f"Use this link to reset your password: {url}"
        )
        mail.send(msg)

        return {
            "message": "Password reset email sent."
        }, 200


    @staticmethod
    def reset_password(data):
        user = User.query.filter_by(reset_token=data["token"]).first()

        if not user or user.reset_token_expiry < datetime.utcnow():
            return {
                "message": "Invalid or expired token"
            }, 400

        user.set_password(data["new_password"])
        user.reset_token = None
        user.reset_token_expiry = None

        db.session.commit()
        return {
            "masseage": "Password reset successfully"
        }, 200
        
