from flask import jsonify, request, Blueprint
from CRUD.expert.model_l2_ref_str import L2RefStringModel

l2_ref_string_blueprint = Blueprint('l2_ref_string_blueprint', __name__)

# READ ALL
@l2_ref_string_blueprint.route('/l2-ref-string', methods=['GET'])
def get_all_l2_ref_string_items():

    items = L2RefStringModel.get_all()
    return jsonify({"l2_ref_string_items": items}), 200

# CREATE
@l2_ref_string_blueprint.route('/l2-ref-string', methods=['POST'])
def create_l2_ref_string_item():

    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    item_lv2_name_en = data.get('item_lv2_name_en')
    normal = data.get('normal')
    borderline = data.get('borderline')
    abnormal = data.get('abnormal')
    notexamined = data.get('notexamined')

    l2_ref_string_item = L2RefStringModel(
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
@l2_ref_string_blueprint.route('/l2-ref-string/<item_id>', methods=['GET'])
def get_l2_ref_string_item_by_id(item_id):

    item = L2RefStringModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_ref_string_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@l2_ref_string_blueprint.route('/l2-ref-string/<item_id>', methods=['PUT'])
def update_l2_ref_string_item(item_id):

    data = request.get_json()

    updated_item = L2RefStringModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Reference String item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@l2_ref_string_blueprint.route('/l2-ref-string/<item_id>', methods=['DELETE'])
def delete_l2_ref_string_item(item_id):

    deleted_item = L2RefStringModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Reference String item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
