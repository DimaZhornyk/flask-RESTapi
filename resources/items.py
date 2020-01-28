from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('store_id', type=int, required=True, help='This field cannot be left blank')

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'An error occurred finding the item'}, 500

        if item:
            return item.json(), 200
        return {'message': "Item doesnt exist"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"Item named {name} already exists"}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return {"message": f"Item {name} successfully added"}, 201

    @jwt_required()
    def put(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'An error occurred finding the item'}, 500

        data = Item.parser.parse_args()
        if item is None:
            item = ItemModel(name, **data)
            item.save_to_db()
            return {'message': f'An item {name} created'}
        else:
            item.price = data['price']
            item.store_id = data['store_id']
            item.save_to_db()
            return {'message': f"{name} was updated"}

    @jwt_required()
    def delete(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'An error occurred finding the item'}, 500
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'No item found with this name'}


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
