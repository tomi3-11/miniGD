from flask_restful import Api
from app.blueprints.files.resources import FileListUploadResource, FileDownloadResource, FileDeleteResource

def register_routes(bp):
    api = Api(bp)

    # add the resources
    api.add_resource(FileListUploadResource, "/upload")
    api.add_resource(FileDeleteResource, "/delete/<file_id>")
    api.add_resource(FileDownloadResource, "/download/<file_id>")
