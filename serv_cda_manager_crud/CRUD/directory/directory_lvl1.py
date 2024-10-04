from . import ( 
DirectoryLevel1,
jsonify,
request,
directory_blueprint
)




# READ ALL 
@directory_blueprint.route('/directory/level1', methods=['GET'])
def get_directory_level1_items():
    items = DirectoryLevel1.get_all()
    return jsonify({"directory_level1_items": items}), 200

# CREATE 
@directory_blueprint.route('/directory/level1', methods=['POST'])
def create_directory_level1_item():
    data = request.get_json()
    
    id = data.get('Id')
    name = data.get('Name')
    name_en = data.get('NameEn')
    acronym = data.get('Acronym')
    display_order = data.get('DisplayOrder')

    directory_level1 = DirectoryLevel1(id, name, name_en, acronym, display_order)
    directory_level1.save_to_db()

    return jsonify({"message": "Directory Level 1 item added successfully"}), 201

# READ by ID
@directory_blueprint.route('/directory/level1/<item_id>', methods=['GET'])
def get_directory_level1_item_by_id(item_id):
    item = DirectoryLevel1.get_by_id(item_id)
    if item:
        return jsonify({"directory_level1_item": item}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# UPDATE 
@directory_blueprint.route('/directory/level1/<item_id>', methods=['PUT'])
def update_directory_level1_item(item_id):
    data = request.get_json()

    updated_item = DirectoryLevel1.update_by_id(item_id, data)
    if updated_item.matched_count > 0:
        return jsonify({"message": "Directory Level 1 item updated successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# DELETE 
@directory_blueprint.route('/directory/level1/<item_id>', methods=['DELETE'])
def delete_directory_level1_item(item_id):
    deleted_item = DirectoryLevel1.delete_by_id(item_id)
    if deleted_item.deleted_count > 0:
        return jsonify({"message": "Directory Level 1 item deleted successfully"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404




