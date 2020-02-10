from flask_restful import Resource
from models.store import StoreModel
from flask_jwt_extended import jwt_required


class Store(Resource):
    @jwt_required
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    @jwt_required
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f'Store with name {name} already exists'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Troubles occurred saving the store'}, 500
        return store.json(), 201

    @jwt_required
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store successfully deleted'}
        return {'message': f'Store with name {name} doesnt exist'}


class StoreList(Resource):
    @jwt_required
    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}
