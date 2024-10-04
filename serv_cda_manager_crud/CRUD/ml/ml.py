
from . import (
jsonify,
request,
ml_blueprint, 
MLModel
)

# READ ALL
@ml_blueprint.route('/ml-models', methods=['GET'])
def get_ml_models():
    """Get all ML models"""
    items = MLModel.get_all()
    return jsonify({"ml_models": items}), 200

# CREATE
@ml_blueprint.route('/ml-models', methods=['POST'])
def create_ml():
    data = request.get_json()

    item_lv3_name_en = data.get('item_lv3_name_en')
    modelname = data.get('modelname')
    label = data.get('label')
    label_name_th = data.get('label_name_th')
    label_name_en = data.get('label_name_en')
    group = data.get('group')
    column = data.get('column')
    category_codes = data.get('category_codes')

    ml_model = MLModel(item_lv3_name_en, modelname, label, label_name_th, label_name_en, group, column, category_codes)
    ml_model.save_to_db()

    return jsonify({"message": "ML model added successfully"}), 201

# READ
@ml_blueprint.route('/ml-models/<item_id>', methods=['GET'])
def get_ml_by_id(item_id):
    """Get a single ML model by its ID"""
    item = MLModel.get_by_id(item_id)
    if item:
        return jsonify({"ml_model": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@ml_blueprint.route('/ml-models/<item_id>', methods=['PUT'])
def update_ml(item_id):
    """Update an ML model by ID"""
    data = request.get_json()

    updated_item = MLModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "ML model updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@ml_blueprint.route('/ml-models/<item_id>', methods=['DELETE'])
def delete_ml_model(item_id):
    """Delete an ML model by ID"""
    deleted_item = MLModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "ML model deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

