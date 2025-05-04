from flask import Blueprint, request, jsonify
from app.models import User, db
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    if user and check_password_hash(user.password, data.get('password')):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200

    return jsonify({"msg": "Invalid credentials"}), 401
