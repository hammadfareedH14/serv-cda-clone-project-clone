
from db_con import connection
import uuid
from bson import ObjectId


# Connect to MongoDB
db = connection.db_client_atlas()
directory_collection_lvl3 = db["directory_level_3"]


class DirectoryLevel3:
    def __init__(self, id, id_lv1, id_lv2, name, name_en, acronym=None, remark=None, instruction=None,
                 status=None, value_min=None, value_max=None, unit=None, price=None, display_order=None,
                 call_name=None, ocare_code=None, order=None):
        
        self.id = id
        self.id_lv1 = id_lv1
        self.id_lv2 = id_lv2
        self.name = name
        self.name_en = name_en
        self.acronym = acronym
        self.remark = remark
        self.instruction = instruction
        self.status = status
        self.value_min = value_min
        self.value_max = value_max
        self.unit = unit
        self.price = price
        self.display_order = display_order
        self.call_name = call_name
        self.ocare_code = ocare_code
        self.order = order

    def save_to_db(self):
        directory_item = {
            'Id': self.id,
            'Id_lv1': self.id_lv1,
            'Id_lv2': self.id_lv2,
            'Name': self.name,
            'NameEn': self.name_en,
            'Acronym': self.acronym,
            'Remark': self.remark,
            'Instruction': self.instruction,
            'Status': self.status,
            'ValueMin': self.value_min,
            'ValueMax': self.value_max,
            'Unit': self.unit,
            'Price': self.price,
            'DisplayOrder': self.display_order,
            'CallName': self.call_name,
            'OcareCode': self.ocare_code,
            'Order': self.order
        }
        return directory_collection_lvl3.insert_one(directory_item)

    @staticmethod
    def update_by_id(item_id, data):
        return directory_collection_lvl3.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return directory_collection_lvl3.delete_one({'_id': ObjectId(item_id)})
    
    @staticmethod
    def get_by_id(_id):
        result = directory_collection_lvl3.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(directory_collection_lvl3.find())
        for result in results:
            result['_id'] = str(result['_id'])  # This ensures ObjectIds are strings
        return results