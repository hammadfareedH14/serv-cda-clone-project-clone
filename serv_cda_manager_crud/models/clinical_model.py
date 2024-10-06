
from db_con import connection
from bson import ObjectId
# Connect to MongoDB
db = connection.db_client_atlas()
clinical_collection = db["model_clinical"]

class ClinicalModel:
    def __init__(self, id_lv3,item_lv3_name_en, item, active=True, logic_type=None, logic=None):
        self.id_lv3=id_lv3
        self.item_lv3_name_en = item_lv3_name_en
        self.item = item
        self.active = active
        self.logic_type = logic_type
        self.logic = logic

    def save_to_db(self):
        clinical_item = {
            'Id_lv3': self.id_lv3,
            'item_lv3_NameEn': self.item_lv3_name_en,
            'item': self.item,
            'active': self.active,
            'logicType': self.logic_type,
            'logic': self.logic
        }
        return clinical_collection.insert_one(clinical_item)

    @staticmethod
    def update_by_id(item_id, data):
        return clinical_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return clinical_collection.delete_one({'_id': ObjectId(item_id)})

    @staticmethod
    def get_by_id(_id):
        result = clinical_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(clinical_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  # This ensures ObjectIds are strings
        return results
