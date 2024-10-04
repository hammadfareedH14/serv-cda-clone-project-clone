from . import connection,ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l3_item_collection = db["l3_item"]

class L3ItemModel:
    def __init__(self, id_lv3, item_lv3_nameen, item_lv3_callname, item):
        self.id_lv3 = id_lv3  
        self.item_lv3_nameen = item_lv3_nameen  
        self.item_lv3_callname = item_lv3_callname  
        self.item = item  

    def save_to_db(self):
        l3_item_data = {
            '_id': ObjectId(),  
            'id_lv3': self.id_lv3,
            'item_lv3_nameen': self.item_lv3_nameen,
            'item_lv3_callname': self.item_lv3_callname,
            'item': self.item 
        }
        return l3_item_collection.insert_one(l3_item_data)

    @staticmethod
    def get_all():
        return list(l3_item_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l3_item_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l3_item_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l3_item_collection.delete_one({'_id': ObjectId(item_id)})
