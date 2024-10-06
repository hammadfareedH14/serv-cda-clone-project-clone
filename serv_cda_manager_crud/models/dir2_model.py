from bson import ObjectId
from db_con import connection
# import uuid

# Connect to MongoDB
db = connection.db_client_atlas()
directory_collection_lvl2 = db["directory_level_2"]


class DirectoryLevel2:
    def __init__(self,Id,id_lv1, name, name_en, acronym=None, description=None, display_order=None):
        self.Id = Id
        self.id_lv1 = id_lv1
        self.name = name
        self.name_en = name_en
        self.acronym = acronym
        self.description = description
        self.display_order = display_order

    def save_to_db(self):
        directory_item = {
            'Id': self.Id,
            'Id_lv1': self.id_lv1,
            'Name': self.name,
            'NameEn': self.name_en,
            'Acronym': self.acronym,
            'Description': self.description,
            'DisplayOrder': self.display_order
        }
        return directory_collection_lvl2.insert_one(directory_item)

    @staticmethod
    def get_all():
        results = list(directory_collection_lvl2.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results

    
    @staticmethod
    def get_by_id(_id):
        result = directory_collection_lvl2.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def update_by_id(_id, data):
        return directory_collection_lvl2.update_one(
            {'_id': ObjectId(_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(_id):
        return directory_collection_lvl2.delete_one({'_id': ObjectId(_id)})
