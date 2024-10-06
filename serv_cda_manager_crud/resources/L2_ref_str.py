from flask import jsonify, request, Blueprint
from models.model_l2_ref_str import L2RefStrModel

L2_ref_str_blueprint = Blueprint('L2_ref_str', __name__)

# READ ALL
@L2_ref_str_blueprint.route('/all', methods=['GET'])
def get_all_l2_ref_string_items():

    items = L2RefStrModel.get_all()
    return jsonify({"l2_ref_string_items": items}), 200

# CREATE
@L2_ref_str_blueprint.route('/create', methods=['POST'])
def create_l2_ref_string_item():

    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    item_lv2_name_en = data.get('item_lv2_name_en')
    normal = data.get('normal')
    borderline = data.get('borderline')
    abnormal = data.get('abnormal')
    notexamined = data.get('notexamined')

    l2_ref_string_item = L2RefStrModel(
        id_lv2,
        item_lv2_name_en,
        normal,
        borderline,
        abnormal,
        notexamined
    )
    l2_ref_string_item.save_to_db()

    return jsonify({"message": "L2 Reference String item added successfully"}), 201

# READ SINGLE
@L2_ref_str_blueprint.route('/<item_id>', methods=['GET'])
def get_l2_ref_string_item_by_id(item_id):

    item = L2RefStrModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_ref_string_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@L2_ref_str_blueprint.route('/<item_id>', methods=['PUT'])
def update_l2_ref_string_item(item_id):

    data = request.get_json()

    updated_item = L2RefStrModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Reference String item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@L2_ref_str_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l2_ref_string_item(item_id):

    deleted_item = L2RefStrModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Reference String item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
