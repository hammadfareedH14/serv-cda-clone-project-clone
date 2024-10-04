from flask import jsonify, request, Blueprint
from model_l3_mapp_uplaod import DirectoryL3UploadMappingModel

# Initialize the blueprint
directory_l3_upload_mapping_blueprint = Blueprint('directory_l3_upload_mapping_blueprint', __name__)

# READ ALL
@directory_l3_upload_mapping_blueprint.route('/l3-upload-mappings', methods=['GET'])
def get_all_upload_mappings():
    """Get all L3 upload mappings"""
    items = DirectoryL3UploadMappingModel.get_all()
    return jsonify({"upload_mappings": items}), 200

# CREATE
@directory_l3_upload_mapping_blueprint.route('/l3-upload-mappings', methods=['POST'])
def create_upload_mapping():

    data = request.get_json()

    organization = data.get('organization')
    item = data.get('item')  # item should be an object

    upload_mapping_item = DirectoryL3UploadMappingModel(
        organization,
        item
    )
    upload_mapping_item.save_to_db()

    return jsonify({"message": "L3 upload mapping added successfully"}), 201

# READ 
@directory_l3_upload_mapping_blueprint.route('/l3-upload-mappings/<item_id>', methods=['GET'])
def get_upload_mapping_by_id(item_id):

    item = DirectoryL3UploadMappingModel.get_by_id(item_id)
    if item:
        return jsonify({"upload_mapping": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@directory_l3_upload_mapping_blueprint.route('/l3-upload-mappings/<item_id>', methods=['PUT'])
def update_upload_mapping(item_id):

    data = request.get_json()

    updated_item = DirectoryL3UploadMappingModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L3 upload mapping updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@directory_l3_upload_mapping_blueprint.route('/l3-upload-mappings/<item_id>', methods=['DELETE'])
def delete_upload_mapping(item_id):

    deleted_item = DirectoryL3UploadMappingModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L3 upload mapping deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
