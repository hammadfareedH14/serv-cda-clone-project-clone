from flask import Blueprint, session, redirect, url_for, render_template , request
from pymongo import MongoClient
import json 
import uuid
from bson import ObjectId
from datetime import datetime
import pytz
import os ;
from dotenv import load_dotenv ;
load_dotenv() 

from db_con import connection
# expert_blueprint = Blueprint('expert', __name__, url_prefix="/Expert/handle")

from . import expert