
from db_con import connection
from bson import ObjectId
# Connect to MongoDB
db = connection.db_client_atlas()
diseasecapture_collection = db["L2_dict_diseasecapture"]

class DiseaseCaptureModel:
    def __init__(self, id_lv2, item_lv2_name_en, diseasecapture):
        self.id_lv2 = id_lv2
        self.item_lv2_name_en = item_lv2_name_en
        self.diseasecapture = diseasecapture

    def save_to_db(self):
        l2_dict_diseasecapture_item = {
            'id_lv2':self.id_lv2 ,
            'item_lv2_name_en': self.item_lv2_name_en,
            'diseasecapture': self.diseasecapture
        }
        return diseasecapture_collection.insert_one(l2_dict_diseasecapture_item)

    @staticmethod
    def update_by_id(item_id, data):
        return diseasecapture_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return diseasecapture_collection.delete_one({'_id': ObjectId(item_id)})

    @staticmethod
    def get_by_id(_id):
        result = diseasecapture_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(diseasecapture_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results
