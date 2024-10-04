from . import ( 
connection, 
uuid, 
ObjectId
              )

# Connect to MongoDB
db = connection.db_client_atlas()
directory_collection_lvl1 = db["directory_level_1"]


class DirectoryLevel1:
    def __init__(self, id, name, name_en, acronym=None, display_order=None):
        self.id = id
        self.name = name
        self.name_en = name_en
        self.acronym = acronym
        self.display_order = display_order

    def save_to_db(self):
        directory_item = {
            '_id': uuid.uuid4().hex,
            'Id': self.id,
            'Name': self.name,
            'NameEn': self.name_en,
            'Acronym': self.acronym,
            'DisplayOrder': self.display_order
        }
        return directory_collection_lvl1.insert_one(directory_item)

    @staticmethod
    def get_all():
        return list(directory_collection_lvl1.find())

    @staticmethod
    def get_by_id(item_id):
        return directory_collection_lvl1.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return directory_collection_lvl1.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return directory_collection_lvl1.delete_one({'_id': ObjectId(item_id)})

