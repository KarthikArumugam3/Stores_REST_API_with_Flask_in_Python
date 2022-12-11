import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel

from schemas import StoreSchema

blp = Blueprint("stores",__name__, description="Operation on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            # return {"message":"Store not found"} 
            abort(404, message="Store not found") 

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            # return {"message":"Store not found"}, 404
            abort(404, message="Store not found") 


@blp.route("/store")
class StoreList(MethodView):

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        # return {"Stores": list(stores.values())} - changed because of @blp.response(200, StoreSchema(many=True))
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):

        store = StoreModel(**store_data)
        
        # # Making sure that the store does not exists already
        # for store in stores.values():
        #     if store_data["name"] == store["name"]:
        #         abort(400, message=f"Store already exists.")

        # store_id = uuid.uuid4().hex                    ### Just a long string of unique characters - ex:- f3f4hkuhsfuiw83y2g4k4
        # store = {**store_data, "id": store_id}  
        # stores[store_id] = store

        
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")

        return store