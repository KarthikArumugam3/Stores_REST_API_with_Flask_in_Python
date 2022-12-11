from db import db

# The SQLAlchemy instance (db) many things that we can use to tell SQLAlchemy what tables we are going to use and what columns those tables will have. 

class StoreModel(db.Model):
    # mapping between a row in a table and class in python

    # Tealling SQLAlchemy we are going to create/use a table called items for this class & all its objects 
    __tablename__ = 'stores'

    # defining columns of the table

    # id - a link b/w the stores table & items(store_id) table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False) # nullable=Fasle - cannot create an item name      
    items = db.relationship("ItemModel",back_populates="store",lazy="dynamic")
   