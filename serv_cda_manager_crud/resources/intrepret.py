
from flask import jsonify, request, Blueprint
from models.model_intrepret import InterpretModel

interpret_blueprint = Blueprint('interpret', __name__)

# READ ALL
@interpret_blueprint.route('/all', methods=['GET'])
def get_all_l2_dict_interpret_items():

    items = InterpretModel.get_all()
    return jsonify({"l2_dict_interpret_items": items}), 200

# CREATE
@interpret_blueprint.route('/create', methods=['POST'])
def create_l2_dict_interpret_item():

    data = request.get_json()

    id_lv2 = data.get('id_lv2')
    item_lv2_name_en = data.get('item_lv2_name_en')
    lv2_condition = data.get('lv2_condition')
    notexamined = data.get('notexamined')
    abnormal = data.get('abnormal')
    normal = data.get('normal')
    borderline = data.get('borderline')
    grade1 = data.get('grade1')
    grade2 = data.get('grade2')
    grade3 = data.get('grade3')
    grade4 = data.get('grade4')
    grade5 = data.get('grade5')
    grade6 = data.get('grade6')

    l2_dict_interpret_item = InterpretModel(
        id_lv2,
        item_lv2_name_en,
        lv2_condition,
        notexamined,
        abnormal,
        normal,
        borderline,
        grade1,
        grade2,
        grade3,
        grade4,
        grade5,
        grade6
    )
    l2_dict_interpret_item.save_to_db()

    return jsonify({"message": "L2 Dictionary Interpretation item added successfully"}), 201

# READ 
@interpret_blueprint.route('/<item_id>', methods=['GET'])
def get_l2_dict_interpret_item_by_id(item_id):

    item = InterpretModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_dict_interpret_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@interpret_blueprint.route('/<item_id>', methods=['PUT'])
def update_l2_dict_interpret_item(item_id):

    data = request.get_json()

    updated_item = InterpretModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Dictionary Interpretation item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@interpret_blueprint.route('/<item_id>', methods=['DELETE'])
def delete_l2_dict_interpret_item(item_id):

    deleted_item = InterpretModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Dictionary Interpretation item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
