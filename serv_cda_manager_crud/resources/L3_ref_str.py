from flask import jsonify, request, Blueprint
from model_l3_ref_str import L3RefStringModel

# Initialize the blueprint
l3_ref_string_blueprint = Blueprint('l3_ref_string_blueprint', __name__)

# READ ALL
@l3_ref_string_blueprint.route('/l3-ref-string', methods=['GET'])
def get_all_l3_ref_string_items():

    items = L3RefStringModel.get_all()
    return jsonify({"l3_ref_string_items": items}), 200

# CREATE
@l3_ref_string_blueprint.route('/l3-ref-string', methods=['POST'])
def create_l3_ref_string_item():
    data = request.get_json()

    id_lv3 = data.get('id_lv3')
    item_lv2_name_en = data.get('item_lv2_name_en')
    item_lv3_call_name = data.get('item_lv3_call_name')
    normal = data.get('normal')
    borderline = data.get('borderline')
    abnormal = data.get('abnormal')
    notexamined = data.get('notexamined')

    l3_ref_string_item = L3RefStringModel(
        id_lv3,
        item_lv2_name_en,
        item_lv3_call_name,
        normal,
        borderline,
        abnormal,
        notexamined
    )
    l3_ref_string_item.save_to_db()

    return jsonify({"message": "L3 Reference String item added successfully"}), 201

# READ SINGLE
@l3_ref_string_blueprint.route('/l3-ref-string/<item_id>', methods=['GET'])
def get_l3_ref_string_item_by_id(item_id):
    """Get a single L3 Reference String item by its ID"""
    item = L3RefStringModel.get_by_id(item_id)
    if item:
        return jsonify({"l3_ref_string_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@l3_ref_string_blueprint.route('/l3-ref-string/<item_id>', methods=['PUT'])
def update_l3_ref_string_item(item_id):
    """Update an L3 Reference String item by ID"""
    data = request.get_json()

    updated_item = L3RefStringModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 Reference String item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@l3_ref_string_blueprint.route('/l3-ref-string/<item_id>', methods=['DELETE'])
def delete_l3_ref_string_item(item_id):
    """Delete an L3 Reference String item by ID"""
    deleted_item = L3RefStringModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 Reference String item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
