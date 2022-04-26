from flask import Flask
from flask_pymongo import pymongo
import certifi

CONNECTION_STRING = "mongodb+srv://CSC735IoT:jwZwjhZvgW308qCq@cluster0.yfejg.mongodb.net/CovidManagement?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
db = client.get_database("CovidManagement")
user_db = pymongo.collection.Collection(db, 'User')
building_db = pymongo.collection.Collection(db, 'Building')
