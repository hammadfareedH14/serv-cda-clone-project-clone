from . import connection,ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l3_upload_mapping_collection = db["directory_l3_upload_mapping"]

class DirectoryL3UploadMappingModel:
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
    def get_all():
        return list(l3_upload_mapping_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l3_upload_mapping_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l3_upload_mapping_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l3_upload_mapping_collection.delete_one({'_id': ObjectId(item_id)})
