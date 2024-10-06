from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
structured_dict_orderitem_collection = db["structured-dict-orderitem"]

class StructuredDictOrderItemModel:
    def __init__(self, GenericName, Type, SynonymName):
        self.GenericName = GenericName
        self.Type = Type
        self.SynonymName = SynonymName

    def save_to_db(self):
        structured_dict_orderitem_item = {
            '_id': uuid.uuid4().hex,
            'GenericName': self.GenericName,
            'Type': self.Type,
            'SynonymName': self.SynonymName
        }
        return structured_dict_orderitem_collection.insert_one(structured_dict_orderitem_item)

    @staticmethod
    def get_all():
        return list(structured_dict_orderitem_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return structured_dict_orderitem_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return structured_dict_orderitem_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return structured_dict_orderitem_collection.delete_one({'_id': ObjectId(item_id)})
