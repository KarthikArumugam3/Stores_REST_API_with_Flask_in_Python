import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema
 
blp = Blueprint("Items","items", description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            # return {"message":"Item not found"}, 404
            abort(404, message="Item not found") 


    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item deleted"}
        except KeyError:
            # return {"message":"Item not found"}, 404
            abort(404, message="Item not found") 

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        # item_data = request.get_json()
        # # There's  more validation to do here!
        # # Like making sure price is a number, and also both items are optional
        # # Difficult to do with an if statement...
        # if "name" not in item_data or "price" not in item_data:
        #     abort(404, message="Bad request. Ensure 'name' and 'price' are included in the JSON payload.")
        try:
            item = items[item_id] 

            # https://blog.teclado.com/python-dictionary-merge-update-operators/
            item |= item_data   #update the new value with old value

            return item
        except KeyError:
            # return {"message":"Item not found"}, 404
            abort(404, message="Item not found") 

@blp.route("/item")
class ItemList(MethodView):
    
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        # return {"items" : list(items.values())} - changed because of @blp.response(200, ItemSchema(many=True))
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self,item_data):
        # item_data = request.get_json()

        # Here not only we need to validate data exists,
        # But also what type of data. Price should be a float,
        # for example.

        
        # Here we check if the data entered already exists or not
        # If it does then we throw a messages
        for item in items.values():

            if (
                item_data['name'] == item['name'] and item_data['store_id'] == item['store_id']
            ):
                abort(404, message=f"Item already exists")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item, 201