
from bson import ObjectId
from db_con import connection

# Connect to MongoDB
db = connection.db_client_atlas()
L3_ref_collection = db["L3_ref"]

class L3RefModel:
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
        return L3_ref_collection.insert_one(l3_item_data)



    @staticmethod
    def update_by_id(item_id, data):
        return L3_ref_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return L3_ref_collection.delete_one({'_id': ObjectId(item_id)})

    @staticmethod
    def get_by_id(_id):
        result = L3_ref_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(L3_ref_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results