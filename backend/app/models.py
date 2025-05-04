from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    username = db.Column(db.String(100), nullable=True)
    oauth_provider = db.Column(db.String(50), nullable=True, index=True)  # 'github', 'google', 'microsoft'
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # One-to-one relationship with password credentials
    credentials = db.relationship(
        "UserCredentials",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email} ({self.oauth_provider or 'local'})>"


class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    password_hash = db.Column(db.String(512), nullable=False)  # Increased for stronger hash support

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Credentials for user_id={self.user_id}>"


# class OAuthToken(db.Model):
#     __tablename__ = 'oauth_tokens'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     provider = db.Column(db.String(50), nullable=False)  # e.g., github, google, microsoft
#     access_token = db.Column(db.Text, nullable=False)
#     refresh_token = db.Column(db.Text, nullable=True)
#     expires_at = db.Column(db.DateTime, nullable=True)

#     user = db.relationship('User', backref='oauth_tokens')

#     def __repr__(self):
#         return f"<OAuthToken {self.provider} for user_id={self.user_id}>"














# from app import db
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime, timezone
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# #user model
# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(120), unique=True, nullable=False, index=True)
#     username = db.Column(db.String(80), unique=True)
#     created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))
#     is_active = db.Column(db.Boolean, default=True)

#     credentials = db.relationship('UserCredentials', backref='user', uselist=False, cascade="all, delete-orphan")
#     auth_providers = db.relationship('AuthProvider', backref='user', cascade="all, delete-orphan")

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             "username": self.username,
#             "created_at": self.created_at.isoformat(),
#             "updated_at": self.updated_at.isoformat() if self.updated_at else None,
#             "is_active": self.is_active
#         }

#     def __repr__(self):
#         return f"<User {self.email}>"

# #user credential model
# class UserCredentials(db.Model):
#     __tablename__ = 'user_credentials'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
#     password_hash = db.Column(db.String(60), nullable=False)

#     user = db.relationship('User', backref='credentials', uselist=False)

#     def set_password(self, password):
#         self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return f"<UserCredentials for user_id={self.user_id}>"

# # OAuth Provider Model
# class AuthProvider(db.Model):
#     __tablename__ = 'auth_providers'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     provider = db.Column(db.String(50), nullable=False)  # e.g., 'github', 'google', 'microsoft'
#     provider_user_id = db.Column(db.Integer, nullable=False)  # ID from the OAuth provider
#     created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
#     updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))
#     is_active = db.Column(db.Boolean, default=True)

#     # Define relationships
#     user = db.relationship('User', backref=db.backref('auth_providers', lazy=True))

#     # Unique constraint for provider and provider_user_id
#     __table_args__ = (
#         db.UniqueConstraint('provider', 'provider_user_id', name='uq_provider_user'),
#         db.Index('ix_provider_user_id', 'provider_user_id')  # Index on provider_user_id for faster lookup
#     )

#     def __repr__(self):
#         return f"<AuthProvider {self.provider}:{self.provider_user_id}>"


