from flask import jsonify, request, Blueprint
from model_l2_dict_intrepret import L2DictInterpretModel

# Initialize the blueprint
l2_dict_interpret_blueprint = Blueprint('l2_dict_interpret_blueprint', __name__)

# READ ALL
@l2_dict_interpret_blueprint.route('/l2-dict-interpret', methods=['GET'])
def get_all_l2_dict_interpret_items():
    """Get all L2 Dictionary Interpretation items"""
    items = L2DictInterpretModel.get_all()
    return jsonify({"l2_dict_interpret_items": items}), 200

# CREATE
@l2_dict_interpret_blueprint.route('/l2-dict-interpret', methods=['POST'])
def create_l2_dict_interpret_item():
    """Create a new L2 Dictionary Interpretation item"""
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

    # Create the L2DictInterpretModel object and save it to the database
    l2_dict_interpret_item = L2DictInterpretModel(
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

# READ SINGLE
@l2_dict_interpret_blueprint.route('/l2-dict-interpret/<item_id>', methods=['GET'])
def get_l2_dict_interpret_item_by_id(item_id):
    """Get a single L2 Dictionary Interpretation item by its ID"""
    item = L2DictInterpretModel.get_by_id(item_id)
    if item:
        return jsonify({"l2_dict_interpret_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@l2_dict_interpret_blueprint.route('/l2-dict-interpret/<item_id>', methods=['PUT'])
def update_l2_dict_interpret_item(item_id):
    """Update an L2 Dictionary Interpretation item by ID"""
    data = request.get_json()

    updated_item = L2DictInterpretModel.update_by_id(item_id, data)

    if updated_item.matched_count > 0:
        return jsonify({"message": "L2 Dictionary Interpretation item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@l2_dict_interpret_blueprint.route('/l2-dict-interpret/<item_id>', methods=['DELETE'])
def delete_l2_dict_interpret_item(item_id):
    """Delete an L2 Dictionary Interpretation item by ID"""
    deleted_item = L2DictInterpretModel.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "L2 Dictionary Interpretation item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
