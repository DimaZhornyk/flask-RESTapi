import os

from datetime import timedelta
from db import db

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.items import Item, ItemList
from resources.user import UserRegister, User, UserLogin, TokenRefresh
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'Flask'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
api = Api(app)

jwt = JWTManager(app)

BLACKLIST = {3}


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['identity'] in BLACKLIST


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}


@jwt.expired_token_loader
def expired_token_callback():
    return {"description": "Token has expired",
            'error': 'token_expired'}, 401


@jwt.invalid_token_loader
def invalid_token_callback():
    return {'error': "invalid token"}, 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return {'description': 'The token has been revoked',
            'error': 'token_revoked'}, 401


api.add_resource(Item, '/item/<string:name>/')
api.add_resource(ItemList, '/items/')
api.add_resource(UserRegister, '/register/')
api.add_resource(Store, '/store/<string:name>/')
api.add_resource(StoreList, '/stores/')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
