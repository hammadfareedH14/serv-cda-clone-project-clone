
from flask import jsonify, request, Blueprint
from struct_dict_order_item_model import StructuredDictOrderItemModel

# Initialize the blueprint
structured_dict_orderitem_blueprint = Blueprint('structured_dict_orderitem_blueprint', __name__)

# READ ALL
@structured_dict_orderitem_blueprint.route('/structured-dict-orderitem', methods=['GET'])
def get_all_structured_dict_orderitems():

    items = StructuredDictOrderItemModel.get_all()
    return jsonify({"structured_dict_orderitems": items}), 200

# CREATE
@structured_dict_orderitem_blueprint.route('/structured-dict-orderitem', methods=['POST'])
def create_structured_dict_orderitem():

    data = request.get_json()

    GenericName = data.get('GenericName')
    Type = data.get('Type')
    SynonymName = data.get('SynonymName')

    structured_dict_orderitem_item = StructuredDictOrderItemModel(
        GenericName,
        Type,
        SynonymName
    )
    structured_dict_orderitem_item.save_to_db()

    return jsonify({"message": "Structured dictionary order item added successfully"}), 201

# READ SINGLE
@structured_dict_orderitem_blueprint.route('/structured-dict-orderitem/<item_id>', methods=['GET'])
def get_structured_dict_orderitem_by_id(item_id):
    """Get a single structured dictionary order item by its ID"""
    item = StructuredDictOrderItemModel.get_by_id(item_id)
    if item:
        return jsonify({"structured_dict_orderitem": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@structured_dict_orderitem_blueprint.route('/structured-dict-orderitem/<item_id>', methods=['PUT'])
def update_structured_dict_orderitem(item_id):
    """Update a structured dictionary order item by ID"""
    data = request.get_json()

    updated_item = StructuredDictOrderItemModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "Structured dictionary order item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@structured_dict_orderitem_blueprint.route('/structured-dict-orderitem/<item_id>', methods=['DELETE'])
def delete_structured_dict_orderitem(item_id):
    """Delete a structured dictionary order item by ID"""
    deleted_item = StructuredDictOrderItemModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Structured dictionary order item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
