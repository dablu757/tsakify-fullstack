from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify, g

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            g.current_user_id = get_jwt_identity()  # Store in Flask global
        except Exception as e:
            return jsonify({"msg": "Missing or invalid token", "error": str(e)}), 401
        return fn(*args, **kwargs)
    return wrapper
