from minio import Minio
from minio.error import S3Error
import uuid


class StorageService:
    def __init__(self):
        self.client = Minio(
            "minio:9000",
            access_key="minioadmin",
            secret_key="minioadmin",
            secure=False
        )
        self.bucket = "files"

    def generate_object_key(self, user_id, file_id, filename):
        return f"{user_id}/{file_id}/{filename}"

    
    def upload_file(self, file, object_key, content_type):
        try:
            self.client.put_object(
               bucket_name= self.bucket,
               object_name=object_key,
               data=file,
               length=1,
               part_size=10 * 1024 * 1024,
               content_type=content_type
            )
        except S3Error as e:
            raise Exception(f"Minio Upload Error: {str(e)}")

    
    def delete_file(self, object_key):
        try:
            self.client.remove_object(self.bucket, object_key)
        except S3Error as e:
            raise Exception(f"Minio Delete Error: {str(e)}")


    def generate_presigned_url(self, object_key):
        return self.client.presigned_get_object(
            self.bucket,
            object_key,
            expires=3600 # 1 hr
        )
