# database.py - functions for managing database

from pymongo import MongoClient

client = MongoClient("mongodb+srv://pavan2827:Pavan2827@mycluster.moxmjqr.mongodb.net/?retryWrites=true&w=majority")

from bson.objectid import ObjectId

stationary_db = client.stationary_db
list_collection = stationary_db.list_collection


def get_items(id=None):
    if id == None:
        items = list_collection.find({})
    else:
        items = list_collection.find({'_id': ObjectId(id)})
    items = [{'id': str(item['_id']), 'description': item['description']} for item in items]
    return items


def add_item(description):
    list_collection.insert_one({'description': description})


def delete_item(id):
    list_collection.delete_one({'_id': ObjectId(id)})


def update_item(id, description):
    list_collection.update_one({'_id': ObjectId(id)}, {'$set': {'description': description}})
