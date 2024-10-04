from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l2_ref_string_collection = db["L2_ref"]

class L2RefStringModel:
    def __init__(self, id_lv2, item_lv2_name_en, normal, borderline, abnormal, notexamined):
        self.id_lv2 = id_lv2
        self.item_lv2_name_en = item_lv2_name_en
        self.normal = normal
        self.borderline = borderline
        self.abnormal = abnormal
        self.notexamined = notexamined

    def save_to_db(self):
        l2_ref_string_item = {
            'Id_lv2': uuid.uuid4().hex,
            'item_lv2_NameEn': self.item_lv2_name_en,
            'normal_list': self.normal,
            'borderline_list': self.borderline,
            'abnormal_list': self.abnormal,
            'notexamined_list': self.notexamined
        }
        return l2_ref_string_collection.insert_one(l2_ref_string_item)

    @staticmethod
    def get_all():
        return list(l2_ref_string_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l2_ref_string_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l2_ref_string_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l2_ref_string_collection.delete_one({'_id': ObjectId(item_id)})
