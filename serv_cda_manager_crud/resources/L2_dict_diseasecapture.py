from flask import jsonify, request, Blueprint
from model_l2_diseasecapture import L2DictDiseaseCaptureModel

l2_dict_blueprint = Blueprint('l2_dict_blueprint', __name__)

# READ ALL
@l2_dict_blueprint.route('/l2-dict', methods=['GET'])
def get_all_l2_dict_items():

    items = L2DictDiseaseCaptureModel.get_all()
    return jsonify({"l2_dict_items": items}), 200

# CREATE
@l2_dict_blueprint.route('/l2-dict', methods=['POST'])
def create_l2_dict_item():

    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    item_lv2_name_en = data.get('item_lv2_name_en')
    diseasecapture = data.get('diseasecapture')

    l2_dict_item = L2DictDiseaseCaptureModel(
        id_lv2,
        item_lv2_name_en,
        diseasecapture
    )
    l2_dict_item.save_to_db()

    return jsonify({"message": "L2 Dictionary Disease Capture item added successfully"}), 201

# READ 
@l2_dict_blueprint.route('/l2-dict/<item_id>', methods=['GET'])
def get_l2_dict_item_by_id(item_id):

    item = L2DictDiseaseCaptureModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_dict_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@l2_dict_blueprint.route('/l2-dict/<item_id>', methods=['PUT'])
def update_l2_dict_item(item_id):

    data = request.get_json()

    updated_item = L2DictDiseaseCaptureModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Dictionary Disease Capture item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@l2_dict_blueprint.route('/l2-dict/<item_id>', methods=['DELETE'])
def delete_l2_dict_item(item_id):

    deleted_item = L2DictDiseaseCaptureModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Dictionary Disease Capture item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
