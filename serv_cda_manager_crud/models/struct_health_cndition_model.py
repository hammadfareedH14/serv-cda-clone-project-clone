
from bson import ObjectId
from db_con import connection

# Connect to MongoDB
db = connection.db_client_atlas()
struct_dict_healthcondition_collection = db["struct-dict-healthcondition"]

class StructDictHealthCondition:
    def __init__(self, GenericName, ICD10, ClinicalCaptureName):
        self.GenericName = GenericName
        self.ICD10 = ICD10
        self.ClinicalCaptureName = ClinicalCaptureName

    def save_to_db(self):
        structured_dict_healthcondition_item = {
            'GenericName': self.GenericName,
            'ICD10': self.ICD10,
            'ClinicalCaptureName': self.ClinicalCaptureName
        }
        return struct_dict_healthcondition_collection.insert_one(structured_dict_healthcondition_item)

 

    @staticmethod
    def update_by_id(item_id, data):
        return struct_dict_healthcondition_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return struct_dict_healthcondition_collection.delete_one({'_id': ObjectId(item_id)})



    @staticmethod
    def get_by_id(_id):
        result = struct_dict_healthcondition_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(struct_dict_healthcondition_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results