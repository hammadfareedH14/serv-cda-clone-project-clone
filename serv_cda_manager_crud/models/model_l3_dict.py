from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l3_dict_collection = db["L3_dict"]

class L3DictModel:
    def __init__(self, id_lv2, id_lv3, item_lv2_name_en, item_lv3_name_en, item_lv3_call_name, undefined, notexamined, abnormal, normal, borderline, under1, under2, over1, over2, overt):
        self.id_lv2 = id_lv2
        self.id_lv3 = id_lv3
        self.item_lv2_name_en = item_lv2_name_en
        self.item_lv3_name_en = item_lv3_name_en
        self.item_lv3_call_name = item_lv3_call_name
        self.undefined = undefined
        self.notexamined = notexamined
        self.abnormal = abnormal
        self.normal = normal
        self.borderline = borderline
        self.under1 = under1
        self.under2 = under2
        self.over1 = over1
        self.over2 = over2
        self.overt = overt

    def save_to_db(self):
        l3_dict_item = {
            'Id_lv2': self.id_lv2,
            'Id_lv3': self.id_lv2,
            'item_lv2_NameEn': self.item_lv2_name_en,
            'item_lv3_NameEn': self.item_lv3_name_en,
            'item_lv3_CallName': self.item_lv3_call_name,
            'undefined': self.undefined,
            'notexamined': self.notexamined,
            'abnormal': self.abnormal,
            'normal': self.normal,
            'borderline': self.borderline,
            'under1': self.under1,
            'under2': self.under2,
            'over1': self.over1,
            'over2': self.over2,
            'overt': self.overt
        }
        return l3_dict_collection.insert_one(l3_dict_item)

    @staticmethod
    def get_all():
        return list(l3_dict_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l3_dict_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l3_dict_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l3_dict_collection.delete_one({'_id': ObjectId(item_id)})
