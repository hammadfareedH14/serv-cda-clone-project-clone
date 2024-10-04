from flask import jsonify, request, Blueprint
from struct_health_cndition_model import StructDictHealthCondition

structured_dict_healthcondition_blueprint = Blueprint('structured_dict_healthcondition_blueprint', __name__)

# READ ALL
@structured_dict_healthcondition_blueprint.route('/structured-dict-healthcondition', methods=['GET'])
def get_all_structured_dict_healthconditions():
    """Get all structured dictionary health conditions"""
    items = StructDictHealthCondition.get_all()
    return jsonify({"structured_dict_healthconditions": items}), 200

# CREATE
@structured_dict_healthcondition_blueprint.route('/structured-dict-healthcondition', methods=['POST'])
def create_structured_dict_healthcondition():
    """Create a new structured dictionary health condition"""
    data = request.get_json()

    GenericName = data.get('GenericName')
    ICD10 = data.get('ICD10')
    ClinicalCaptureName = data.get('ClinicalCaptureName')

    structured_dict_healthcondition_item = StructDictHealthCondition(
        GenericName,
        ICD10,
        ClinicalCaptureName
    )
    structured_dict_healthcondition_item.save_to_db()

    return jsonify({"message": "Structured dictionary health condition added successfully"}), 201

# READ 
@structured_dict_healthcondition_blueprint.route('/structured-dict-healthcondition/<item_id>', methods=['GET'])
def get_structured_dict_healthcondition_by_id(item_id):
    item = StructDictHealthCondition.get_by_id(item_id)
    if item:
        return jsonify({"structured_dict_healthcondition": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@structured_dict_healthcondition_blueprint.route('/structured-dict-healthcondition/<item_id>', methods=['PUT'])
def update_structured_dict_healthcondition(item_id):

    data = request.get_json()

    updated_item = StructDictHealthCondition.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "Structured dictionary health condition updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@structured_dict_healthcondition_blueprint.route('/structured-dict-healthcondition/<item_id>', methods=['DELETE'])
def delete_structured_dict_healthcondition(item_id):

    deleted_item = StructDictHealthCondition.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Structured dictionary health condition deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
