
from flask import jsonify, request, Blueprint
from models.struct_dict_order_model import StructDictOrderItemModel


struct_dict_orderitem_blueprint = Blueprint('struct_dict_orderitem', __name__)

# READ ALL
@struct_dict_orderitem_blueprint.route('/all', methods=['GET'])
def get_all_structured_dict_orderitems():

    items = StructDictOrderItemModel.get_all()
    return jsonify({"structured_dict_orderitems": items}), 200

# CREATE
@struct_dict_orderitem_blueprint.route('/create', methods=['POST'])
def create_structured_dict_orderitem():

    data = request.get_json()

    GenericName = data.get('GenericName')
    Type = data.get('Type')
    SynonymName = data.get('SynonymName')

    structured_dict_orderitem_item =StructDictOrderItemModel(
        GenericName,
        Type,
        SynonymName
    )
    structured_dict_orderitem_item.save_to_db()

    return jsonify({"message": "Structured dictionary order item added successfully"}), 201

# READ SINGLE
@struct_dict_orderitem_blueprint.route('/<item_id>', methods=['GET'])
def get_structured_dict_orderitem_by_id(item_id):

    item = StructDictOrderItemModel.get_by_id(item_id)
    if item:
        return jsonify({"structured_dict_orderitem": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@struct_dict_orderitem_blueprint.route('/<item_id>', methods=['PUT'])
def update_structured_dict_orderitem(item_id):

    data = request.get_json()

    updated_item = StructDictOrderItemModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "Structured dictionary order item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@struct_dict_orderitem_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_structured_dict_orderitem(item_id):

    deleted_item = StructDictOrderItemModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Structured dictionary order item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
