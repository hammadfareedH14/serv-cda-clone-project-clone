#imports start
from flask import Blueprint,session, redirect, url_for, render_template , request
from pymongo import MongoClient
import json 
from bson import ObjectId
from datetime import datetime
import pytz
import os ;
#imprts end

from db_con import connection
import uuid
from bson import ObjectId
from dotenv import load_dotenv

# model.py file
from pymongo import MongoClient
from bson import ObjectId
import uuid
from db_con import connection
# clinical.py
from flask import Flask, request, jsonify
from bson import ObjectId

load_dotenv()

# clinical_blueprint = Blueprint('clinical', __name__, url_prefix="/Clinical/handle")

# from . import clinical