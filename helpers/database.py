
from pymongo import MongoClient
from flask import session
client = MongoClient("mongodb://localhost:27017")
data = client['mile12']
users=data['users']