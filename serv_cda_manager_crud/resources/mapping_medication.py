from flask import jsonify, request, Blueprint
from model_mapping_medication import MappMedicationModel

# Initialize the blueprint
medication_blueprint = Blueprint('medication_blueprint', __name__)

# READ ALL
@medication_blueprint.route('/medications', methods=['GET'])
def get_all_medications():
    """Get all medications"""
    items = MappMedicationModel.get_all()
    return jsonify({"medications": items}), 200

# CREATE
@medication_blueprint.route('/medications', methods=['POST'])
def create_medication():
    """Create a new medication"""
    data = request.get_json()

    GenericName = data.get('GenericName')
    Name_TH = data.get('Name_TH')
    RegName = data.get('RegName')

    medication_item = MappMedicationModel(
        GenericName,
        Name_TH,
        RegName
    )
    medication_item.save_to_db()

    return jsonify({"message": "Medication added successfully"}), 201

# READ SINGLE
@medication_blueprint.route('/medications/<item_id>', methods=['GET'])
def get_medication_by_id(item_id):
    """Get a single medication by its ID"""
    item = MappMedicationModel.get_by_id(item_id)
    if item:
        return jsonify({"medication": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@medication_blueprint.route('/medications/<item_id>', methods=['PUT'])
def update_medication(item_id):
    """Update a medication by ID"""
    data = request.get_json()

    updated_item = MappMedicationModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "Medication updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@medication_blueprint.route('/medications/<item_id>', methods=['DELETE'])
def delete_medication(item_id):
    """Delete a medication by ID"""
    deleted_item = MappMedicationModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Medication deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
