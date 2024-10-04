from . import connection,uuid,ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
clinical_collection = db["model_clinical"]
# directory_collection_lvl3 = db["directory_level_3"]

class ClinicalModel:
    def __init__(self, item_lv3_name_en, item, active=True, logic_type=None, logic=None):
        self.item_lv3_name_en = item_lv3_name_en
        self.item = item
        self.active = active
        self.logic_type = logic_type
        self.logic = logic

    def save_to_db(self):
        clinical_item = {
            'Id_lv3': uuid.uuid4().hex,
            'item_lv3_NameEn': self.item_lv3_name_en,
            'item': self.item,
            'active': self.active,
            'logicType': self.logic_type,
            'logic': self.logic
        }
        return clinical_collection.insert_one(clinical_item)

    @staticmethod
    def get_all():
        return list(clinical_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return clinical_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return clinical_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return clinical_collection.delete_one({'_id': ObjectId(item_id)})
