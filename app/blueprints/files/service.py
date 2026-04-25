import uuid
from flask import abort
from app import db
from app.models import File
from app.blueprints.storage.service import StorageService

storage = StorageService()


class FileService:
    
    @staticmethod
    def upload_file(file, current_user_id):
        file_id = str(uuid.uuid4())

        object_key = storage.generate_object_key(
            current_user_id,
            file_id,
            file.filename
        )

        # Upload to minio
        try:
            storage.upload_file(
                file.stream,
                object_key=object_key,
                content_type=file.content_type
            )
        except Exception as e:
            abort(500, str(e))
            
        # Save metadata
        new_file = File(
            id=file_id,
            filename=file.filename,
            object_key=object_key,
            bucket_name="files",
            size=0, 
            content_type=file.content_type,
            owner_id=current_user_id
        )

        try:
            db.session.add(new_file)
            db.session.commit()
        except Exception:
            # rollback MinIO if Db fails
            storage.delete_file(object_key)
            abort(500, "Database error")

        return new_file


    @staticmethod
    def get_user_files(user_id):
        return File.query.filter_by(owner_id=user_id).all()


    @staticmethod
    def delete_file(file_id, user_id):
        file = File.query.get_or_404(file_id)

        if not file or file.owner_id != user_id:
            abort(403, "Unauthorized")

        storage.delete_file(file.object_key)

        db.session.delete(file)
        db.session.commit()


    @staticmethod
    def get_download_url(file_id, user_id):
        file = File.query.get_or_404(file_id)

        if not file or file.owner_id != user_id:
            abort(403, "Unauthorized")

        return storage.generate_presigned_url(file.object_key)
