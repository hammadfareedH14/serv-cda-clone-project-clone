from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l2_dict_collection = db["L2_dict"]

class L2DictModel:
    def __init__(self, id_lv2, item_lv2_name_en, lv2_condition, undefined, abnormal, normal, borderline):
        self.id_lv2 = id_lv2
        self.item_lv2_name_en = item_lv2_name_en
        self.lv2_condition = lv2_condition
        self.undefined = undefined
        self.abnormal = abnormal
        self.normal = normal
        self.borderline = borderline

    def save_to_db(self):
        l2_dict_item = {
            'Id_lv2': uuid.uuid4().hex,
            'item_lv2_NameEn': self.item_lv2_name_en,
            'lv2_condition': self.lv2_condition,
            'undefined': self.undefined,
            'abnormal': self.abnormal,
            'normal': self.normal,
            'borderline': self.borderline
        }
        return l2_dict_collection.insert_one(l2_dict_item)

    @staticmethod
    def get_all():
        return list(l2_dict_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l2_dict_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l2_dict_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l2_dict_collection.delete_one({'_id': ObjectId(item_id)})
