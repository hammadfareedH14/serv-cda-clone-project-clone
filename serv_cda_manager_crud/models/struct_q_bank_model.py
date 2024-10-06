from . import connection, uuid, ObjectId

# Connect to MongoDB
db = connection.db_client_atlas()
structured_q_bank_collection = db["structured-q-bank"]

class StructuredQBankModel:
    def __init__(self, LN, Intention, SubIntention, Type, Tag, Q, A):
        self.LN = LN
        self.Intention = Intention
        self.SubIntention = SubIntention
        self.Type = Type
        self.Tag = Tag
        self.Q = Q
        self.A = A

    def save_to_db(self):
        structured_q_bank_item = {
            '_id': uuid.uuid4().hex,
            'LN': self.LN,
            'Intention': self.Intention,
            'SubIntention': self.SubIntention,
            'Type': self.Type,
            'Tag': self.Tag,
            'Q': self.Q,
            'A': self.A
        }
        return structured_q_bank_collection.insert_one(structured_q_bank_item)

    @staticmethod
    def get_all():
        return list(structured_q_bank_collection.find())

    @staticmethod
    def get_by_id(item_id):
        return structured_q_bank_collection.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_by_id(item_id, data):
        return structured_q_bank_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': data}
        )

    @staticmethod
    def delete_by_id(item_id):
        return structured_q_bank_collection.delete_one({'_id': ObjectId(item_id)})
