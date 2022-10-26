# database.py - functions for managing database

import dataset

db = dataset.connect('sqlite:///shopping_list.db')

def get_items(id=None):
    table = db['list']
    if id == None:
        items = table.find()
    else:
        items = table.find(id=int(id))
    items = [dict(item) for item in items]
    return items

def add_item(description, quantity):
    db.begin()
    try:
        table = db['list']
        item = { "description": description, "quantity": int(quantity)}
        table.insert(item)
        db.commit()
    except:
        db.rollback()

def delete_item(id):
    db.begin()
    try:
        table = db['list']
        table.delete(id=int(id))
        db.commit()
    except:
        db.rollback()

def update_item(id, description):
    db.begin()
    try:
        table = db['list']
        new_data = {'id':int(id), 'description':description}
        table.update(new_data, ['id'])
        db.commit()
    except:
        db.rollback()
