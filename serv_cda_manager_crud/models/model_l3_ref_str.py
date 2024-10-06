from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l3_ref_string_collection = db["L3_ref"]

class L3RefStringModel:
    def __init__(self, id_lv3, item_lv2_name_en, item_lv3_call_name, normal, borderline, abnormal, notexamined):
        self.id_lv3 = id_lv3
        self.item_lv2_name_en = item_lv2_name_en
        self.item_lv3_call_name = item_lv3_call_name
        self.normal = normal
        self.borderline = borderline
        self.abnormal_ = abnormal
        self.notexamined = notexamined

    def save_to_db(self):
        l3_ref_string_item = {
            'Id_lv3': uuid.uuid4().hex,
            'item_lv2_NameEn': self.item_lv2_name_en,
            'item_lv3_CallName': self.item_lv3_call_name,
            'normal_list': self.normal_list,
            'borderline_list': self.borderline_list,
            'abnormal_list': self.abnormal_list,
            'notexamined_list': self.notexamined_list
        }
        return l3_ref_string_collection.insert_one(l3_ref_string_item)

    @staticmethod
    def get_all():
        return list(l3_ref_string_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l3_ref_string_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l3_ref_string_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l3_ref_string_collection.delete_one({'_id': ObjectId(item_id)})
