from flask import jsonify, request, Blueprint
from models.model_diseasecapture import DiseaseCaptureModel

DiseaseCapture_blueprint = Blueprint('diseasecapture', __name__)

# READ ALL
@DiseaseCapture_blueprint.route('/all', methods=['GET'])
def get_all_l2_dict_items():

    items = DiseaseCaptureModel.get_all()
    return jsonify({"l2_dict_items": items}), 200

# CREATE
@DiseaseCapture_blueprint.route('/create', methods=['POST'])
def create_l2_dict_item():

    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    item_lv2_name_en = data.get('item_lv2_name_en')
    diseasecapture = data.get('diseasecapture')

    l2_dict_item = DiseaseCaptureModel(
        id_lv2,
        item_lv2_name_en,
        diseasecapture
    )
    l2_dict_item.save_to_db()

    return jsonify({"message": "L2 Dictionary Disease Capture item added successfully"}), 201

# READ 
@DiseaseCapture_blueprint.route('/<item_id>', methods=['GET'])
def get_l2_dict_item_by_id(item_id):

    item = DiseaseCaptureModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_dict_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@DiseaseCapture_blueprint.route('/<item_id>', methods=['PUT'])
def update_l2_dict_item(item_id):

    data = request.get_json()

    updated_item = DiseaseCaptureModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Dictionary Disease Capture item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@DiseaseCapture_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l2_dict_item(item_id):

    deleted_item = DiseaseCaptureModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Dictionary Disease Capture item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
