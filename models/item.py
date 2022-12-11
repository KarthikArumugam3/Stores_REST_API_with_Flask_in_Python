from db import db

# The SQLAlchemy instance (db) many things that we can use to tell SQLAlchemy what tables we are going to use and what columns those tables will have. 

class ItemModel(db.Model):
    # mapping between a row in a table and class in python

    # Tealling SQLAlchemy we are going to create/use a table called items for this class & all its objects 
    __tablename__ = 'items'

    # defining columns of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False) # nullable=Fasle - cannot create an item name      
    price = db.Column(db.Float(precision=2), nullable=False)

    # store__id(foreign key) - a link b/w the items table & stores table
    store_id = db.Column(db.Integer,db.ForeignKey("stores.id"), unique=False, nullable=False)
    
    store = db.relationship("StoreModel",back_populates="items")