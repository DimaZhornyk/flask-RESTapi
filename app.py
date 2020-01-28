import os

from datetime import timedelta
from db import db

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from security import *
from resources.items import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList
from templates import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Flask'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>/')
api.add_resource(ItemList, '/items/')
api.add_resource(UserRegister, '/register/')
api.add_resource(Store, '/store/<string:name>/')
api.add_resource(StoreList, '/stores/')


@app.route('/')
def home():
    return render_template('index.html')


db.init_app(app)
if __name__ == '__main__':
    app.run(debug=False)
