from db_con import connection
from bson import ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
L2_ref_str_collection = db["L2_ref_str"]

class L2RefStrModel:
    def __init__(self, id_lv2, item_lv2_name_en, normal, borderline, abnormal, notexamined):
        self.id_lv2 = id_lv2
        self.item_lv2_name_en = item_lv2_name_en
        self.normal = normal
        self.borderline = borderline
        self.abnormal = abnormal
        self.notexamined = notexamined

    def save_to_db(self):
        l2_ref_string_item = {
            'id_lv2': self.id_lv2,
            'item_lv2_name_en': self.item_lv2_name_en,
            'normal_list': self.normal,
            'borderline_list': self.borderline,
            'abnormal_list': self.abnormal,
            'notexamined_list': self.notexamined
        }
        return L2_ref_str_collection.insert_one(l2_ref_string_item)


    @staticmethod
    def update_by_id(item_id, data):
        return L2_ref_str_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return L2_ref_str_collection.delete_one({'_id': ObjectId(item_id)})


    @staticmethod
    def get_by_id(_id):
        result = L2_ref_str_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(L2_ref_str_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results