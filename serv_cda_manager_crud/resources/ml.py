
from models.ML_model import MLModel
from flask import request,jsonify,Blueprint

ML_blueprint = Blueprint('ML', __name__)

# READ ALL
@ML_blueprint.route('/all', methods=['GET'])
def get_ml_models():

    items = MLModel.get_all()
    return jsonify({"ml_models": items}), 200

# CREATE
@ML_blueprint.route('/ml-create', methods=['POST'])
def create_ml():
    data = request.get_json()
    
    Id_lv3 = data.get('Id_lv3') 
    item_lv3_name_en = data.get('item_lv3_name_en')
    modelname = data.get('modelname')
    label = data.get('label')
    label_name = data.get('label_name')
    group = data.get('group')
    column = data.get('column')
    category_codes = data.get('category_codes')

    ml_model = MLModel( Id_lv3,item_lv3_name_en, modelname,label,label_name,group, column, category_codes)
    ml_model.save_to_db()

    return jsonify({"message": "ML model added successfully"}), 201

# READ
@ML_blueprint.route('/<item_id>', methods=['GET'])
def get_ml_by_id(item_id):

    item = MLModel.get_by_id(item_id)
    if item:
        return jsonify({"ml_model": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@ML_blueprint.route('<item_id>', methods=['PUT'])
def update_ml(item_id):

    data = request.get_json()

    updated_item = MLModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "ML model updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@ML_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_ml_model(item_id):

    deleted_item = MLModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "ML model deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

