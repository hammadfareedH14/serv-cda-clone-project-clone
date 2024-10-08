
from flask import Blueprint,request,jsonify

from models.clinical_model import ClinicalModel

clinical_blueprint = Blueprint('clinical', __name__)

# READ ALL
@clinical_blueprint.route('/clinical-items', methods=['GET'])
def get_clinical_items():
    items = ClinicalModel.get_all()
    return jsonify({"clinical_items": items}), 200


@clinical_blueprint.route('/clinical-items', methods=['POST'])
def create_clinical_item():

    data = request.get_json()
    id_lv3 = data.get('id_lv3')
    item_lv3_name_en = data.get('item_lv3_name_en') 
    item = data.get('item')
    active = data.get('active', True)
    logic_type = data.get('logic_type')  
    logic = data.get('logic')

    clinical_model = ClinicalModel(id_lv3, item_lv3_name_en, item, active, logic_type, logic)
    clinical_model.save_to_db()

    return jsonify({"message": "Clinical item added successfully"}), 201


# READ
@clinical_blueprint.route('/clinical-items/<item_id>', methods=['GET'])
def get_clinical_item_by_id(item_id):
    item = ClinicalModel.get_by_id(item_id)
    
    if item:
        # Convert _id to string
        # item['_id'] = str(item['_id'])
        return jsonify({"clinical_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
# UPDATE
@clinical_blueprint.route('/clinical-items/<item_id>', methods=['PUT'])
def update_clinical_item(item_id):
    data = request.get_json()

    updated_item = ClinicalModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "Clinical item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@clinical_blueprint.route('/clinical-items/<item_id>', methods=['DELETE'])
def delete_clinical_item(item_id):
    deleted_item = ClinicalModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Clinical item deleted successfully"}),200
    else:
        return jsonify({"message": "Item not found"}),404


