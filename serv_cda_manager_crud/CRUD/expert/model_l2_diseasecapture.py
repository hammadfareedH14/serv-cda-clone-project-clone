from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l2_dict_diseasecapture_collection = db["L2_dict_diseasecapture"]

class L2DictDiseaseCaptureModel:
    def __init__(self, id_lv2, item_lv2_name_en, diseasecapture):
        self.id_lv2 = id_lv2
        self.item_lv2_name_en = item_lv2_name_en
        self.diseasecapture = diseasecapture

    def save_to_db(self):
        l2_dict_diseasecapture_item = {
            'Id_lv2': uuid.uuid4().hex,
            'item_lv2_NameEn': self.item_lv2_name_en,
            'diseasecapture': self.diseasecapture
        }
        return l2_dict_diseasecapture_collection.insert_one(l2_dict_diseasecapture_item)

    @staticmethod
    def get_all():
        return list(l2_dict_diseasecapture_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l2_dict_diseasecapture_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l2_dict_diseasecapture_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l2_dict_diseasecapture_collection.delete_one({'_id': ObjectId(item_id)})
