
from flask import request,jsonify,Blueprint
from models.dir3_model import  DirectoryLevel3
directory_blueprint_lv3 = Blueprint('directory3', __name__)


# READ ALL 
@directory_blueprint_lv3.route('/all', methods=['GET'])
def get_directory_level3_items():
    items = DirectoryLevel3.get_all()
    return jsonify({"directory_level3_items": items}), 200

# CREATE 
@directory_blueprint_lv3.route('/create', methods=['POST'])
def create_directory_level3_item():
    data = request.get_json()

    id = data.get('Id')
    id_lv1 = data.get('Id_lv1')
    id_lv2 = data.get('Id_lv2')
    name = data.get('Name')
    name_en = data.get('NameEn')
    acronym = data.get('Acronym')
    remark = data.get('Remark')
    instruction = data.get('Instruction')
    status = data.get('Status')
    value_min = data.get('ValueMin')
    value_max = data.get('ValueMax')
    unit = data.get('Unit')
    price = data.get('Price')
    display_order = data.get('DisplayOrder')
    call_name = data.get('CallName')
    ocare_code = data.get('OcareCode')
    order = data.get('Order')

    directory_level3 = DirectoryLevel3(id, id_lv1, id_lv2, name, name_en, acronym, remark, instruction, status, 
                                    value_min, value_max, unit, price, display_order, call_name, ocare_code, order)
    directory_level3.save_to_db()

    return jsonify({"message": "Directory Level 3 item added successfully"}), 201

# READ  by ID
@directory_blueprint_lv3.route('/<item_id>', methods=['GET'])
def get_directory_level3_item_by_id(item_id):
    item = DirectoryLevel3.get_by_id(item_id)
    if item:
        return jsonify({"directory_level3_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE 
@directory_blueprint_lv3.route('/<item_id>', methods=['PUT'])
def update_directory_level3_item(item_id):
    data = request.get_json()

    updated_item = DirectoryLevel3.update_by_id(item_id, data)
    if updated_item.matched_count > 0:
        return jsonify({"message": "Directory Level 3 item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE 
@directory_blueprint_lv3.route('/<item_id>', methods=['DELETE'])
def delete_directory_level3_item(item_id):
    deleted_item = DirectoryLevel3.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Directory Level 3 item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

