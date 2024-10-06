from flask import jsonify, request, Blueprint
from models.struct_q_bank_model import StructQBankModel

# Initialize the blueprint
struct_q_bank_blueprint = Blueprint('struct_q_bank_blueprint', __name__)

# READ ALL
@struct_q_bank_blueprint.route('/all', methods=['GET'])
def get_all_structured_q_bank_items():

    items = StructQBankModel.get_all()
    return jsonify({"structured_q_bank_items": items}), 200

# CREATE
@struct_q_bank_blueprint.route('/create', methods=['POST'])
def create_structured_q_bank_item():
    data = request.get_json()

    LN = data.get('LN')
    Intention = data.get('Intention')
    SubIntention = data.get('SubIntention')
    Type = data.get('Type')
    Tag = data.get('Tag')
    Q = data.get('Q')
    A = data.get('A')

    structured_q_bank_item = StructQBankModel(
        LN,
        Intention,
        SubIntention,
        Type,
        Tag,
        Q,
        A
    )
    structured_q_bank_item.save_to_db()

    return jsonify({"message": "Structured question bank item added successfully"}), 201

# READ SINGLE
@struct_q_bank_blueprint.route('/<item_id>', methods=['GET'])
def get_structured_q_bank_item_by_id(item_id):

    item =StructQBankModel.get_by_id(item_id)
    if item:
        return jsonify({"structured_q_bank_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@struct_q_bank_blueprint.route('/<item_id>', methods=['PUT'])
def update_structured_q_bank_item(item_id):

    data = request.get_json()

    updated_item = StructQBankModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "Structured question bank item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@struct_q_bank_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_structured_q_bank_item(item_id):

    deleted_item =StructQBankModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Structured question bank item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
