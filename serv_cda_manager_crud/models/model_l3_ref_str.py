
from bson import ObjectId
from db_con import connection

# Connect to MongoDB
db = connection.db_client_atlas()
L3_ref_str_collection = db["L3_ref_str"]

class L3RefStrModel:
    def __init__(self, id_lv3, item_lv2_name_en, item_lv3_call_name, normal_list,
                borderline_list, abnormal_list, notexamined_list):
        
        self.id_lv3 = id_lv3
        self.item_lv2_name_en = item_lv2_name_en
        self.item_lv3_call_name = item_lv3_call_name
        self.normal_list = normal_list
        self.borderline_list = borderline_list
        self.abnormal_list = abnormal_list
        self.notexamined_list = notexamined_list

    def save_to_db(self):
        l3_ref_string_item = {
            'id_lv3': self.id_lv3,
            'item_lv2_name_en': self.item_lv2_name_en,
            'item_lv3_CallName': self.item_lv3_call_name,
            'normal_list': self.normal_list,
            'borderline_list': self.borderline_list,
            'abnormal_list': self.abnormal_list,
            'notexamined_list': self.notexamined_list
        }
        return L3_ref_str_collection.insert_one(l3_ref_string_item)


    @staticmethod
    def update_by_id(item_id, data):
        return L3_ref_str_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return L3_ref_str_collection.delete_one({'_id': ObjectId(item_id)})

    @staticmethod
    def get_by_id(_id):
        result = L3_ref_str_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(L3_ref_str_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results