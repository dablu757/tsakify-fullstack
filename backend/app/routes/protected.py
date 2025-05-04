# from flask import Blueprint, g, jsonify
# from app.utils.jwt import login_required
# from app.models import User

# protected_bp = Blueprint('protected', __name__)

# @protected_bp.route('/dashboard', methods=['GET'])
# @login_required
# def dashboard():
#     user = User.query.get(g.current_user_id)
#     return jsonify({
#         "message": f"Welcome {user.email}!",
#         "user_id": user.id
#     })
