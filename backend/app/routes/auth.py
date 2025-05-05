#write by myself for learning purpose
from flask import Blueprint, request
from app.utils.response import success_response, error_response
from app.models import User, UserCredentials, db
from werkzeug.exceptions import BadRequest
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token,
    get_jwt_identity
)

from datetime import timedelta
import os
from app.utils.jwt import token_required


auth_bp = Blueprint('auth', __name__)

#health route
@auth_bp.route('/health')
def health():
    return success_response(message='OK')

#registation route
@auth_bp.route("/register", methods = ['POST'])
def user_register():
    
    data = request.get_json()
    _userName = data.get('username')
    _email = data.get('email')
    _password = data.get('password')

    if not _email or not _password:
        return error_response(message="Email and password are required")
   
    if '@' not in _email or '.' not in _email:
        return error_response(message="Invalid email format")
  
    isUserExist = User.query.filter_by(email = _email).first()

    if isUserExist:
        return error_response(message="User already exists")
  
    try:
        _user = User(email = _email, username = _userName)
        db.session.add(_user)
        db.session.flush() #flush to generate user_id
       
        _credentials = UserCredentials(user_id = _user.id)
        _credentials.set_password(password=_password)
      
        db.session.add(_credentials)
        db.session.commit()
        return success_response(message="User registered successfully",status_code=201)
    
    except BadRequest as br:
        db.session.rollback()  # Rollback if there's a bad request error
        return error_response(message=str(br), status_code=400)
    except Exception as e:
        db.session.rollback()  # Rollback any other errors
        return error_response(message=f"An error occurred: {str(e)}", status_code=500)
    
#login route
@auth_bp.route("/login", methods = ['POST'])
def user_login():

    data = request.get_json()
    _email = data.get('email')
    _password = data.get('password')

    if not _email or not _password:
        return error_response(message="Email and password are required")
    
    try :
        user = User.query.filter_by(email=_email).first()
        if not user or not user.credentials or not user.credentials.check_password(_password):
            return error_response(message="Invalid credentials")
        
        access_exp = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES", 15)))
        refresh_exp = timedelta(days=int(os.getenv("REFRESH_TOKEN_EXPIRES_DAYS", 30)))

        access_token = create_access_token(identity=user.id, expires_delta=access_exp)
        refresh_token = create_refresh_token(identity=user.id, expires_delta=refresh_exp)

        return success_response(
            message="login successfull",
            status_code=200,
            data={
                'user' : user.id,
                'access_token' : access_token,
                'refresh_token' : refresh_token
            }
        )
    except BadRequest as br:
        return error_response(message=str(br), status_code=400)

    except Exception as e:
        return error_response(message="Internal server error", status_code=500)
    
#user profile
@auth_bp.route("/profile", methods=['GET'])
@token_required
def user_profile():
    user_id = get_jwt_identity()
    return success_response(message="Success", data={"user_id": user_id})

    

    

# from datetime import timedelta
# from app.utils.jwt import token_required  # Custom @token_required decorator

# auth_bp = Blueprint('auth', __name__)

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
