
from flask import jsonify, request, Blueprint
from models.model_l3_mapp_uplaod import Dir3UploadMappingModel

# Initialize the blueprint
dir3_upload_mapping_blueprint = Blueprint('dir3_upload_mapp', __name__)

# READ ALL
@dir3_upload_mapping_blueprint.route('/all', methods=['GET'])
def get_all_upload_mappings():

    items = Dir3UploadMappingModel.get_all()
    return jsonify({"upload_mappings": items}), 200

# CREATE
@dir3_upload_mapping_blueprint.route('/create', methods=['POST'])
def create_upload_mapping():

    data = request.get_json()

    organization = data.get('organization')
    item = data.get('item')  

    upload_mapping_item = Dir3UploadMappingModel(
        organization,
        item
    )
    upload_mapping_item.save_to_db()

    return jsonify({"message": "L3 upload mapping added successfully"}), 201

# READ 
@dir3_upload_mapping_blueprint.route('/<item_id>', methods=['GET'])
def get_upload_mapping_by_id(item_id):

    item =Dir3UploadMappingModel.get_by_id(item_id)
    if item:
        return jsonify({"upload_mapping": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@dir3_upload_mapping_blueprint.route('/<item_id>', methods=['PUT'])
def update_upload_mapping(item_id):

    data = request.get_json()

    updated_item = Dir3UploadMappingModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 upload mapping updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@dir3_upload_mapping_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_upload_mapping(item_id):

    deleted_item = Dir3UploadMappingModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 upload mapping deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
