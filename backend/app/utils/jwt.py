# from functools import wraps
# from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
# from flask import jsonify, g

# def login_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         try:
#             verify_jwt_in_request()
#             g.current_user_id = get_jwt_identity()  # Store in Flask global
#         except Exception as e:
#             return jsonify({"msg": "Missing or invalid token", "error": str(e)}), 401
#         return fn(*args, **kwargs)
#     return wrapper



from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask import jsonify

def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            # Verify the JWT in the request
            verify_jwt_in_request()
        except Exception as e:
            # Return a 401 Unauthorized response if JWT verification fails
            return jsonify({"msg": "Token is missing or invalid", "error": str(e)}), 401

        # Proceed with the original function call if the token is valid
        return fn(*args, **kwargs)

    return wrapper
