from flask import jsonify, request, Blueprint
from model_l3_dict import L3DictModel

# Initialize the blueprint
l3_dict_blueprint = Blueprint('l3_dict_blueprint', __name__)

# READ ALL
@l3_dict_blueprint.route('/l3-dict', methods=['GET'])
def get_all_l3_dict_items():
    """Get all L3 Dictionary items"""
    items = L3DictModel.get_all()
    return jsonify({"l3_dict_items": items}), 200

# CREATE
@l3_dict_blueprint.route('/l3-dict', methods=['POST'])
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

# READ SINGLE
@l3_dict_blueprint.route('/l3-dict/<item_id>', methods=['GET'])
def get_l3_dict_item_by_id(item_id):
    """Get a single L3 Dictionary item by its ID"""
    item = L3DictModel.get_by_id(item_id)
    if item:
        return jsonify({"l3_dict_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@l3_dict_blueprint.route('/l3-dict/<item_id>', methods=['PUT'])
def update_l3_dict_item(item_id):
    """Update an L3 Dictionary item by ID"""
    data = request.get_json()

    updated_item = L3DictModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 Dictionary item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@l3_dict_blueprint.route('/l3-dict/<item_id>', methods=['DELETE'])
def delete_l3_dict_item(item_id):

    deleted_item = L3DictModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 Dictionary item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
