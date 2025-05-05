from flask import jsonify
from typing import Any, Optional, Dict, Tuple


def success_response(
    message: str,
    data: Optional[Dict[str, Any]] = None,
    status_code: int = 200
) -> Tuple[Any, int]:
    
    response = {
        "status": "success",
        "message": message
    }

    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


def error_response(
    message: str,
    error_code: Optional[str] = None,
    status_code: int = 400
) -> Tuple[Any, int]:
    
    response = {
        "status": "error",
        "message": message
    }

    if error_code:
        response["error_code"] = error_code

    return jsonify(response), status_code
