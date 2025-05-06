# from functools import wraps
# from flask_jwt_extended import verify_jwt_in_request
# from app.utils.response import error_response
# from app_logging import LOGGER

# def token_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         LOGGER.info(f"wrapper Invocked")
#         try:
#             verify_jwt_in_request()
#             LOGGER.info(f"verify_jwt_in_request done")
#         except Exception as e:
#             return error_response(
#                 message=f"Token is missing or invalid.",
#                 status_code=401
#             )
#         return fn(*args, **kwargs)
#     return wrapper

from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from app.utils.response import error_response
from app_logging import LOGGER

def token_required(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        LOGGER.info("token_required: Attempting to verify JWT token.")
        try:
            verify_jwt_in_request()
            LOGGER.info("token_required: JWT verification successful.")
        except (NoAuthorizationError, InvalidHeaderError) as jwt_error:
            LOGGER.warning(f"token_required: JWT verification failed - {str(jwt_error)}")
            return error_response(
                message="Token is missing or invalid.",
                status_code=401
            )
        except Exception as e:
            LOGGER.error(f"token_required: Unexpected error - {str(e)}")
            return error_response(
                message="Something went wrong with token verification.",
                status_code=500
            )
        return fn(*args, **kwargs)
    return decorated_function

