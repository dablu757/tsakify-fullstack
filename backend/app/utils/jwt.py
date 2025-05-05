from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from app.utils.response import error_response

def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception as e:
            return error_response(
                message=f"Token is missing or invalid.",
                status_code=401
            )
        return fn(*args, **kwargs)
    return wrapper
