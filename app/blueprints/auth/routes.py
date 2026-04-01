from .resources import RegisterResource, LoginResource, TokenRefreshResource, CurrentUserResource, PasswordResetRequestResource, PasswordResetConfirmResource, LogoutResource
from flask_restful import Api

def register_blueprint(bp):
    api = Api(bp)

    # add resources
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.add_resource(TokenRefreshResource, "/token/refresh")
    api.add_resource(CurrentUserResource, "/me")
    api.add_resource(PasswordResetConfirmResource, "/password/reset/confirm")
    api.add_resource(PasswordResetRequestResource, "/password/reset")
    api.add_resource(LogoutResource, "/logout")
