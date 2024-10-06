
from bson import ObjectId
from db_con import connection

# Connect to MongoDB
db = connection.db_client_atlas()
l3_upload_mapping_collection = db["dir3_upload_mapping"]

class Dir3UploadMappingModel:
    def __init__(self, organization, item):
        self.organization = organization
        self.item = item  

    def save_to_db(self):
        l3_upload_mapping_item = {
            '_id': ObjectId(),  
            'organization': self.organization,
            'item': self.item 
        }
        return l3_upload_mapping_collection.insert_one(l3_upload_mapping_item)


    @staticmethod
    def update_by_id(item_id, data):
        return l3_upload_mapping_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l3_upload_mapping_collection.delete_one({'_id': ObjectId(item_id)})


    @staticmethod
    def get_by_id(_id):
        result = l3_upload_mapping_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(l3_upload_mapping_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results