from flask import jsonify, request, Blueprint
from models.model_l3_ref_str import L3RefStrModel

# Initialize the blueprint
L3_ref_str_blueprint = Blueprint('L3_ref_str', __name__)

# READ ALL
@L3_ref_str_blueprint.route('/all', methods=['GET'])
def get_all_l3_ref_string_items():

    items = L3RefStrModel.get_all()
    return jsonify({"l3_ref_string_items": items}), 200

# CREATE
@L3_ref_str_blueprint.route('/create', methods=['POST'])
def create_l3_ref_string_item():
    data = request.get_json()

    id_lv3 = data.get('id_lv3')
    item_lv2_name_en = data.get('item_lv2_name_en')
    item_lv3_call_name = data.get('item_lv3_call_name')
    normal_list = data.get('normal_list')
    borderline_list = data.get('borderline_list')
    abnormal_list = data.get('abnormal_list')
    notexamined_list = data.get('notexamined_list')

    l3_ref_string_item = L3RefStrModel(
        id_lv3,
        item_lv2_name_en,
        item_lv3_call_name,
        normal_list,
        borderline_list,
        abnormal_list,
        notexamined_list
    )
    l3_ref_string_item.save_to_db()

    return jsonify({"message": "L3 Reference String item added successfully"}), 201

# READ 
@L3_ref_str_blueprint.route('/<item_id>', methods=['GET'])
def get_l3_ref_string_item_by_id(item_id):

    item =L3RefStrModel.get_by_id(item_id)
    if item:
        return jsonify({"l3_ref_string_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@L3_ref_str_blueprint.route('/<item_id>', methods=['PUT'])
def update_l3_ref_string_item(item_id):

    data = request.get_json()

    updated_item = L3RefStrModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 Reference String item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@L3_ref_str_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l3_ref_string_item(item_id):

    deleted_item = L3RefStrModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 Reference String item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
