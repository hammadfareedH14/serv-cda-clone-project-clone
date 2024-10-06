from . import connection,ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
medication_collection = db["mapping_medication"]

class MappMedicationModel:
    def __init__(self, GenericName, Name_TH, RegName):
        self.GenericName = GenericName
        self.Name_TH = Name_TH
        self.RegName = RegName

    def save_to_db(self):
        medication_item = {
            '_id': ObjectId(),  
            'GenericName': self.GenericName,
            'Name_TH': self.Name_TH,
            'RegName': self.RegName
        }
        return medication_collection.insert_one(medication_item)

    @staticmethod
    def get_all():
        return list(medication_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return medication_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return medication_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return medication_collection.delete_one({'_id': ObjectId(item_id)})
