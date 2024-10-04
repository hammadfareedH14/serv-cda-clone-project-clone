
# from app.routes.gateway import gateway_blueprint
# from app.routes.directory import directory_blueprint
from CRUD.clinical.clinical import clinical_blueprint
# from app.routes.expert import expert_blueprint
# from app.routes.ml import ml_blueprint
# from app.routes.json import json_blueprint
# from app.routes.dataset import dataset_blueprint
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'your_secret_key_here'


import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

PORT = os.getenv('PORT')

CORS(app)

# app.register_blueprint(gateway_blueprint)
# app.register_blueprint(directory_blueprint,url_prefix="/directory")
app.register_blueprint(clinical_blueprint,url_prefix="/clinical")
# app.register_blueprint(expert_blueprint)
# app.register_blueprint(ml_blueprint)
# app.register_blueprint(json_blueprint)
# app.register_blueprint(dataset_blueprint)

# app.register_blueprint(directory_bp, url_prefix='/Directory/handle')
# app.register_blueprint(clinical_bp, url_prefix='/Clinical/handle')
# app.register_blueprint(expert_bp, url_prefix='/Expert/handle')
# # app.register_blueprint(ml_bp, url_prefix='/Ml/handle')
# app.register_blueprint(ml_bp, url_prefix='/ML/handle')

# app.register_blueprint(json_bp, url_prefix='/DataApi')

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
