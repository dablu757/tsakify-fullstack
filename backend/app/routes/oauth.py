from flask import Blueprint, redirect, url_for, jsonify
from authlib.integrations.flask_client import OAuth
from app import db
from app.models import User
from flask_jwt_extended import create_access_token

oauth_bp = Blueprint('oauth', __name__)
oauth = OAuth()

@oauth_bp.record_once
def init_oauth(setup_state):
    app = setup_state.app
    oauth.init_app(app)

    oauth.register(
        name='github',
        client_id=app.config['GITHUB_CLIENT_ID'],
        client_secret=app.config['GITHUB_CLIENT_SECRET'],
        access_token_url='https://github.com/login/oauth/access_token',
        access_token_params=None,
        authorize_url='https://github.com/login/oauth/authorize',
        api_base_url='https://api.github.com/',
        client_kwargs={'scope': 'user:email'},
    )
    # Repeat for Google and Microsoft

@oauth_bp.route('/github')
def github_login():
    redirect_uri = url_for('oauth.github_callback', _external=True)
    return oauth.github.authorize_redirect(redirect_uri)

@oauth_bp.route('/github/callback')
def github_callback():
    token = oauth.github.authorize_access_token()
    resp = oauth.github.get('user', token=token)
    profile = resp.json()

    user = User.query.filter_by(email=profile['email']).first()
    if not user:
        user = User(email=profile['email'], oauth_provider='github')
        db.session.add(user)
        db.session.commit()

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)
