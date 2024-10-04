from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
l2_dict_interpret_collection = db["L2_dict_interpret"]

class L2DictInterpretModel:
    def __init__(self, id_lv2, item_lv2_name_en, lv2_condition, notexamined, abnormal, normal, borderline, grade1, grade2, grade3, grade4, grade5, grade6):
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
            'Id_lv2': uuid.uuid4().hex,
            'item_lv2_NameEn': self.item_lv2_name_en,
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
        return l2_dict_interpret_collection.insert_one(l2_dict_interpret_item)

    @staticmethod
    def get_all():
        return list(l2_dict_interpret_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return l2_dict_interpret_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return l2_dict_interpret_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return l2_dict_interpret_collection.delete_one({'_id': ObjectId(item_id)})
