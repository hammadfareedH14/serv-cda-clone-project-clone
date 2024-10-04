from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
ml_collection = db["model_ml"]

class MLModel:
    def __init__(self, item_lv3_name_en, modelname, label, label_name,group, column, category_codes):
        self.item_lv3_name_en = item_lv3_name_en
        self.modelname = modelname
        self.label = label
        self.label_name_th = label_name
        self.group = group
        self.column = column
        self.category_codes = category_codes

    def save_to_db(self):
        ml_item = {
            'Id_lv3': uuid.uuid4().hex,
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
    def get_all():
        return list(ml_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return ml_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return ml_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return ml_collection.delete_one({'_id': ObjectId(item_id)})
