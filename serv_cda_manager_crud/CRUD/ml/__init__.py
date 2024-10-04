# imports start
from flask import Blueprint, session, redirect, url_for, render_template , request,jsonify
from pymongo import MongoClient
import json 
import uuid
from bson import ObjectId
from datetime import datetime
import pytz
import os ;
from dotenv import load_dotenv;
# imports end

# model.py
from db_con import connection


# ml.py
from model import MLModel  # Import your MLModel class
ml_blueprint = Blueprint('ml', __name__,  url_prefix="/ML/handle")

# load enviroment file
load_dotenv() 


from . import ml
