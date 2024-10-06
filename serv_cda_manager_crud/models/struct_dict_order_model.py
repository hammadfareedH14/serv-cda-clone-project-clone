
from bson import ObjectId
from db_con import connection

# Connect to MongoDB
db = connection.db_client_atlas()
struct_dict_orderitem_collection = db["struct-dict-orderitem"]

class StructDictOrderItemModel:
    def __init__(self, GenericName, Type, SynonymName):
        self.GenericName = GenericName
        self.Type = Type
        self.SynonymName = SynonymName

    def save_to_db(self):
        structured_dict_orderitem_item = {
            'GenericName': self.GenericName,
            'Type': self.Type,
            'SynonymName': self.SynonymName
        }
        return struct_dict_orderitem_collection.insert_one(structured_dict_orderitem_item)


    @staticmethod
    def update_by_id(item_id, data):
        return struct_dict_orderitem_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return struct_dict_orderitem_collection.delete_one({'_id': ObjectId(item_id)})


    @staticmethod
    def get_by_id(_id):
        result = struct_dict_orderitem_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(struct_dict_orderitem_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results