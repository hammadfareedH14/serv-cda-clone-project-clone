
from db_con import connection
from bson import ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
interpret_collection = db["L2_dict_interpret"]

class InterpretModel:
    def __init__(self, id_lv2, item_lv2_name_en, lv2_condition, notexamined, abnormal, normal, borderline,
                grade1, grade2, grade3, grade4, grade5, grade6):
        
        self.id_lv2 = id_lv2
        self.item_lv2_name_en = item_lv2_name_en
        self.lv2_condition = lv2_condition
        self.notexamined = notexamined
        self.abnormal = abnormal
        self.normal = normal
        self.borderline = borderline
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4
        self.grade5 = grade5
        self.grade6 = grade6

    def save_to_db(self):
        l2_dict_interpret_item = {
            'id_lv2 ': self.id_lv2,
            'item_lv2_name_en': self.item_lv2_name_en,
            'lv2_condition': self.lv2_condition,
            'notexamined': self.notexamined,
            'abnormal': self.abnormal,
            'normal': self.normal,
            'borderline': self.borderline,
            'grade1': self.grade1,
            'grade2': self.grade2,
            'grade3': self.grade3,
            'grade4': self.grade4,
            'grade5': self.grade5,
            'grade6': self.grade6
        }
        return interpret_collection.insert_one(l2_dict_interpret_item)


    @staticmethod
    def update_by_id(item_id, data):
        return interpret_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return interpret_collection.delete_one({'_id': ObjectId(item_id)})

    @staticmethod
    def get_by_id(_id):
        result = interpret_collection.find_one({'_id': ObjectId(_id)})
        if result:
            result['_id'] = str(result['_id'])  
        return result
    
    @staticmethod
    def get_all():
        results = list(interpret_collection.find())
        for result in results:
            result['_id'] = str(result['_id'])  
        return results