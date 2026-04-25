from app import db
from datetime import datetime, UTC
import uuid
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    reset_token = db.Column(db.String(255), nullable=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = db.Column(db.String, nullable=False)
    object_key = db.Column(db.String, nullable=False)
    bucket_name = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer)
    content_type = db.Column(db.String)
    owner_id = db.Column(db.String, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now(UTC))

