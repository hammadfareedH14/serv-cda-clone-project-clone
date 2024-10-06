
from db_con import connection
from bson import ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
ml_collection = db["model_ml"]

class MLModel:
    def __init__(self,Id_lv3,item_lv3_name_en, modelname, label, label_name,group, column, category_codes):

        self.Id_lv3 = Id_lv3
        self.item_lv3_name_en = item_lv3_name_en
        self.modelname = modelname
        self.label = label
        self.label_name = label_name
        self.group = group
        self.column = column
        self.category_codes = category_codes

    def save_to_db(self):
        ml_item = {
            'Id_lv3': self.Id_lv3,
            'item_lv3_NameEn': self.item_lv3_name_en,
            'modelname': self.modelname,
            'label': self.label,
            'label_name': self.label_name,
            'group': self.group,
            'column': self.column,
            'category_codes': self.category_codes
        }
        return ml_collection.insert_one(ml_item)

    @staticmethod
    def update_by_id(item_id, data):
        return ml_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return ml_collection.delete_one({'_id': ObjectId(item_id)})
    
    @staticmethod
    def get_by_id(_id):
        result = ml_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(ml_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  # This ensures ObjectIds are strings
        return results