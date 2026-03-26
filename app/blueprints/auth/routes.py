from .resources import RegisterResource, LoginResource, TokenRefreshResource, CurrentUserResource
from flask_restful import Api

def register_blueprint(bp):
    api = Api(bp)

    # add resources
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.add_resource(TokenRefreshResource, "/token/refresh")
    api.add_resource(CurrentUserResource, "/me")
