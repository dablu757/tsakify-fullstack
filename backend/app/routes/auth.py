#write by myself for learning purpose
from flask import Blueprint


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/health')
def health():
    return "ok"











#final copy from gpt

# from flask import Blueprint, request, jsonify
# from app.models import User, UserCredentials, db
# from flask_jwt_extended import (
#     create_access_token,
#     create_refresh_token,
#     get_jwt_identity
# )
# from datetime import timedelta
# from app.utils.jwt import token_required  # Custom @token_required decorator

# auth_bp = Blueprint('auth', __name__)

# #REGISTER
# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     username = data.get('username')

#     if not email or not password:
#         return jsonify({"msg": "Email and password are required"}), 400

#     if User.query.filter_by(email=email).first():
#         return jsonify({"msg": "User already exists"}), 409

#     user = User(email=email, username=username)
#     credentials = UserCredentials(user=user)
#     credentials.set_password(password)

#     db.session.add(user)
#     db.session.add(credentials)
#     db.session.commit()

#     return jsonify({"msg": "User registered successfully"}), 201

# #LOGIN
# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     user = User.query.filter_by(email=email).first()

#     if not user or not user.credentials or not user.credentials.check_password(password):
#         return jsonify({"msg": "Invalid credentials"}), 401

#     access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=15))
#     refresh_token = create_refresh_token(identity=user.id, expires_delta=timedelta(days=30))

#     return jsonify(access_token=access_token, refresh_token=refresh_token), 200

# #REFRESH TOKEN
# @auth_bp.route('/refresh', methods=['POST'])
# @token_required(refresh=True)
# def refresh():
#     current_user_id = get_jwt_identity()
#     new_access_token = create_access_token(identity=current_user_id, expires_delta=timedelta(minutes=15))
#     return jsonify(access_token=new_access_token), 200

# # PROFILE ROUTE
# @auth_bp.route('/profile', methods=['GET'])
# @token_required()
# def profile():
#     current_user_id = get_jwt_identity()
#     user = User.query.get(current_user_id)

#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     return jsonify({
#         "id": user.id,
#         "email": user.email,
#         "username": user.username,
#         "provider": user.oauth_provider or "local",
#         "created_at": user.created_at.isoformat()
#     }), 200



















# from flask import Blueprint, request, jsonify
# from app.models import User, UserCredentials, db
# from flask_jwt_extended import (
#     create_access_token,
#     create_refresh_token,
#     get_jwt_identity
# )
# from datetime import timedelta
# from app.utils.jwt import token_required  # Import the custom decorator

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     username = data.get('username')

#     if not email or not password:
#         return jsonify({"msg": "Email and password are required"}), 400

#     if User.query.filter_by(email=email).first():
#         return jsonify({"msg": "User already exists"}), 409

#     user = User(email=email, username=username)
#     credentials = UserCredentials(user=user)
#     credentials.set_password(password)

#     db.session.add(user)
#     db.session.add(credentials)
#     db.session.commit()

#     return jsonify({"msg": "User registered successfully"}), 201


# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     user = User.query.filter_by(email=email).first()

#     if not user or not user.credentials or not user.credentials.check_password(password):
#         return jsonify({"msg": "Invalid credentials"}), 401

#     access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=15))
#     refresh_token = create_refresh_token(identity=user.id, expires_delta=timedelta(days=30))

#     return jsonify(access_token=access_token, refresh_token=refresh_token), 200


# @auth_bp.route('/refresh', methods=['POST'])
# @token_required  # Use the custom token_required decorator here
# def refresh():
#     current_user_id = get_jwt_identity()
#     new_access_token = create_access_token(identity=current_user_id, expires_delta=timedelta(minutes=15))
#     return jsonify(access_token=new_access_token), 200


# @auth_bp.route('/profile', methods=['GET'])
# @token_required  # Protect this route with the custom token_required decorator
# def profile():
#     current_user_id = get_jwt_identity()
#     user = User.query.get(current_user_id)
#     if not user:
#         return jsonify({"msg": "User not found"}), 404
#     return jsonify({"msg": f"Welcome {user.username}!", "email": user.email}), 200















# from flask import Blueprint, request, jsonify
# from app.models import User, db
# from flask_jwt_extended import create_access_token
# from werkzeug.security import check_password_hash

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(email=data.get('email')).first()

#     if user and check_password_hash(user.password, data.get('password')):
#         token = create_access_token(identity=user.id)
#         return jsonify(access_token=token), 200

#     return jsonify({"msg": "Invalid credentials"}), 401
