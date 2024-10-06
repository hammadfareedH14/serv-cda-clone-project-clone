
# from app.routes.gateway import gateway_blueprint
from resources.directory_lvl1 import directory_blueprint_lv1
from resources.directory_lvl2 import directory_blueprint_lv2
from resources.directory_lvl3 import directory_blueprint_lv3
from resources.clinical import clinical_blueprint
from resources.ml import ML_blueprint
from resources.intrepret import interpret_blueprint
from resources.diseasecapture import DiseaseCapture_blueprint
from resources.L2_dict import l2_dict_blueprint
from resources.L3_dict import L3_dict_blueprint
from resources.L2_ref_str import L2_ref_str_blueprint
from resources.L3_ref_str import L3_ref_str_blueprint
from resources.L3_ref import L3_ref_blueprint
from resources.mapping_medication import medication_blueprint
from resources.dir3_mapp_upload import dir3_upload_mapping_blueprint
from resources.struct_dic_order_item import struct_dict_orderitem_blueprint
from resources.struct_dict_health_condi import structured_dict_healthcondition_blueprint
from resources.struct_q_bank import struct_q_bank_blueprint



from flask import Flask
# from flask_cors import CORS

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'your_secret_key_here'


import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

PORT = os.getenv('PORT')

# CORS(app)

app.register_blueprint(directory_blueprint_lv1,url_prefix="/directory1")
app.register_blueprint(directory_blueprint_lv2,url_prefix="/directory2")
app.register_blueprint(directory_blueprint_lv3,url_prefix="/directory3")
app.register_blueprint(clinical_blueprint,url_prefix="/clinical")
app.register_blueprint(ML_blueprint,url_prefix="/ML")
app.register_blueprint(interpret_blueprint,url_prefix="/interpret")
app.register_blueprint(DiseaseCapture_blueprint,url_prefix="/diseasecapture")
app.register_blueprint(l2_dict_blueprint,url_prefix="/L2_dict")
app.register_blueprint(L3_dict_blueprint,url_prefix="/L3_dict")
app.register_blueprint(L2_ref_str_blueprint,url_prefix="/L2_ref_str")
app.register_blueprint(L3_ref_str_blueprint,url_prefix="/L3_ref_str")
app.register_blueprint(L3_ref_blueprint,url_prefix="/L3_ref")
app.register_blueprint(medication_blueprint,url_prefix="/mapp_medication")
app.register_blueprint(dir3_upload_mapping_blueprint,url_prefix="/dir3_upload_mapp")
app.register_blueprint(struct_dict_orderitem_blueprint,url_prefix="/struct_dict_orderitem")
app.register_blueprint(structured_dict_healthcondition_blueprint,url_prefix="/struct_dict_healthcondition")
app.register_blueprint(struct_q_bank_blueprint,url_prefix="/struct_q_bank")







if __name__ == "__main__":
    app.run(port=PORT, debug=True)
