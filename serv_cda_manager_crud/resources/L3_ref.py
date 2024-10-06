from flask import jsonify, request, Blueprint
from models.model_l3_ref import L3RefModel

L3_ref_blueprint = Blueprint('L3_ref', __name__)

# READ ALL
@L3_ref_blueprint.route('/all', methods=['GET'])
def get_all_l3_items():

    items =L3RefModel.get_all()
    return jsonify({"l3_items": items}), 200

# CREATE
@L3_ref_blueprint.route('/create', methods=['POST'])
def create_l3_item():

    data = request.get_json()

    id_lv3 = data.get('id_lv3')
    item_lv3_nameen = data.get('item_lv3_nameen')
    item_lv3_callname = data.get('item_lv3_callname')
    item = data.get('item') 

    l3_item = L3RefModel(
        id_lv3,
        item_lv3_nameen,
        item_lv3_callname,
        item
    )
    l3_item.save_to_db()

    return jsonify({"message": "L3 item added successfully"}), 201

# READ SINGLE
@L3_ref_blueprint.route('/<item_id>', methods=['GET'])
def get_l3_item_by_id(item_id):

    item = L3RefModel.get_by_id(item_id)
    if item:
        return jsonify({"l3_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@L3_ref_blueprint.route('/<item_id>', methods=['PUT'])
def update_l3_item(item_id):

    data = request.get_json()

    updated_item = L3RefModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@L3_ref_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l3_item(item_id):

    deleted_item = L3RefModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
