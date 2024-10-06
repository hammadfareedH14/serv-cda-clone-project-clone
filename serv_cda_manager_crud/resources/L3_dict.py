from flask import jsonify, request, Blueprint
from models.model_l3_dict import L3DictModel

L3_dict_blueprint = Blueprint('l3_dict', __name__)

# READ ALL
@L3_dict_blueprint.route('/all', methods=['GET'])
def get_all_l3_dict_items():

    items = L3DictModel.get_all()
    return jsonify({"l3_dict_items": items}), 200

# CREATE
@L3_dict_blueprint.route('/create', methods=['POST'])
def create_l3_dict_item():
    """Create a new L3 Dictionary item"""
    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    id_lv3 = data.get('id_lv3')

    item_lv2_name_en = data.get('item_lv2_name_en')
    item_lv3_name_en = data.get('item_lv3_name_en')
    item_lv3_call_name = data.get('item_lv3_call_name')
    undefined = data.get('undefined')
    notexamined = data.get('notexamined')
    abnormal = data.get('abnormal')
    normal = data.get('normal')
    borderline = data.get('borderline')
    under1 = data.get('under1')
    under2 = data.get('under2')
    over1 = data.get('over1')
    over2 = data.get('over2')
    overt = data.get('overt')

    l3_dict_item = L3DictModel(
        id_lv2,
        id_lv3,  
        item_lv2_name_en,
        item_lv3_name_en,
        item_lv3_call_name,
        undefined,
        notexamined,
        abnormal,
        normal,
        borderline,
        under1,
        under2,
        over1,
        over2,
        overt
    )
    l3_dict_item.save_to_db()

    return jsonify({"message": "L3 Dictionary item added successfully"}), 201

# READ 
@L3_dict_blueprint.route('/<item_id>', methods=['GET'])
def get_l3_dict_item_by_id(item_id):

    item = L3DictModel.get_by_id(item_id)
    if item:
        return jsonify({"l3_dict_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@L3_dict_blueprint.route('/<item_id>', methods=['PUT'])
def update_l3_dict_item(item_id):

    data = request.get_json()

    updated_item = L3DictModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 Dictionary item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@L3_dict_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l3_dict_item(item_id):

    deleted_item = L3DictModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 Dictionary item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
