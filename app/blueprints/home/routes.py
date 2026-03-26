from .resource import HomeResource
from flask_restful import Api


def register_blueprint(bp):
    api = Api(bp)

    api.add_resource(HomeResource, "/")

        
