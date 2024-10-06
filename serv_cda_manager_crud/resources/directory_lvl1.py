from models.dir1_model import DirectoryLevel1  # Ensure this import is correct
from flask import Blueprint, request, jsonify

directory_blueprint_lv1 = Blueprint('directory1', __name__)

# READ ALL
@directory_blueprint_lv1.route('/all', methods=['GET'])
def get_directory_level1_items():
    items = DirectoryLevel1.get_all()  # Call the class method directly
    return jsonify({"directory_level1_items": items}), 200

# CREATE
@directory_blueprint_lv1.route('/create', methods=['POST'])
def create_directory_level1_item():
    data = request.get_json()

    # Assign values to variables
    Id = data.get("Id")
    name = data.get("Name")
    name_en = data.get("NameEn")
    acronym = data.get("Acronym")
    display_order = data.get("DisplayOrder")

    # Create a new DirectoryLevel1 item
    directory_level1 = DirectoryLevel1(Id, name=name, name_en=name_en, acronym=acronym, display_order=display_order)
    
    try:
        directory_level1.save_to_db()  # Persist the item to the database
        return jsonify({"message": "Directory Level 1 item added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# READ by ID
@directory_blueprint_lv1.route('/<item_id>', methods=['GET'])
def get_directory_level1_item_by_id(item_id):
    item = DirectoryLevel1.get_by_id(item_id)  # Directly call the class method
    if item:
        return jsonify({"directory_level1_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE
@directory_blueprint_lv1.route('/<item_id>', methods=['PUT'])
def update_directory_level1_item(item_id):
    data = request.get_json()
    updated_item = DirectoryLevel1.update_by_id(item_id, data)  # Directly call the class method

    if updated_item.matched_count > 0:
        return jsonify({"message": "Directory Level 1 item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE
@directory_blueprint_lv1.route('/<item_id>', methods=['DELETE'])
def delete_directory_level1_item(item_id):
    deleted_item = DirectoryLevel1.delete_by_id(item_id)  # Directly call the class method

    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Directory Level 1 item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404
