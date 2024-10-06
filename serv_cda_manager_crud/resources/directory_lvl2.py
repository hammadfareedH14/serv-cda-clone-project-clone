
from flask import Blueprint,request,jsonify
from models.dir2_model import DirectoryLevel2;


directory_blueprint_lv2 = Blueprint('directory2', __name__)


@directory_blueprint_lv2.route('/all', methods=['GET'])
def get_directory_level2_items():
    items = DirectoryLevel2.get_all()
    return jsonify({"directory_level2_items": items}), 200



# CREATE
@directory_blueprint_lv2.route('/create', methods=['POST'])  
def create_directory_level2_item():
    data = request.get_json()

    Id = data.get('Id')
    id_lv1 = data.get('Id_lv1')
    name = data.get('Name')
    name_en = data.get('NameEn')
    acronym = data.get('Acronym')
    description = data.get('Description')
    display_order = data.get('DisplayOrder')

    directory_level2 = DirectoryLevel2(Id, id_lv1, name, name_en, acronym, description, display_order)
    directory_level2.save_to_db()

    return jsonify({"message": "Directory Level 2 item added successfully"}), 201


# READ by ID
@directory_blueprint_lv2.route('/<item_id>', methods=['GET'])
def get_directory_level2_item(item_id):
    item = DirectoryLevel2.get_by_id(item_id)  
    if item:
        return jsonify(item), 200  
    else:
        return jsonify({"message": "Item not found"}), 404 

# UPDATE 
@directory_blueprint_lv2.route('/<item_id>', methods=['PUT'])
def update_directory_level2_item(item_id):
    data = request.get_json()

    updated_item = DirectoryLevel2.update_by_id(item_id, data)
    if updated_item.matched_count > 0:
        return jsonify({"message": "Directory Level 2 item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE 
@directory_blueprint_lv2.route('/<item_id>', methods=['DELETE'])
def delete_directory_level2_item(item_id):
    deleted_item = DirectoryLevel2.delete_by_id(item_id)
    
    # If the item_id was invalid or no item was deleted, handle it
    if deleted_item is None:
        return jsonify({"message": "Invalid item ID format"}), 400  # Return a 'Bad Request' status for invalid ID
    elif deleted_item.deleted_count > 0:
        return jsonify({"message": "Directory Level 2 item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404