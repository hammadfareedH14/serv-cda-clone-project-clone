from flask import jsonify, request, Blueprint
from models.model_l2_dict import L2DictModel

l2_dict_blueprint = Blueprint('l2_dict', __name__)

# READ ALL
@l2_dict_blueprint.route('/all', methods=['GET'])
def get_all_l2_dict_items():

    items = L2DictModel.get_all()
    return jsonify({"l2_dict_items": items}), 200

# CREATE
@l2_dict_blueprint.route('/create', methods=['POST'])
def create_l2_dict_item():

    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    item_lv2_name_en = data.get('item_lv2_name_en')
    lv2_condition = data.get('lv2_condition')
    undefined = data.get('undefined')
    abnormal = data.get('abnormal')
    normal = data.get('normal')
    borderline = data.get('borderline')

    l2_dict_item = L2DictModel(id_lv2, item_lv2_name_en, lv2_condition, undefined, abnormal, normal, borderline)
    l2_dict_item.save_to_db()

    return jsonify({"message": "L2 Dictionary item added successfully"}), 201

# READ SINGLE
@l2_dict_blueprint.route('/<item_id>', methods=['GET'])
def get_l2_dict_item_by_id(item_id):

    item = L2DictModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_dict_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@l2_dict_blueprint.route('/<item_id>', methods=['PUT'])
def update_l2_dict_item(item_id):

    data = request.get_json()

    updated_item = L2DictModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Dictionary item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@l2_dict_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l2_dict_item(item_id):

    deleted_item = L2DictModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Dictionary item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
