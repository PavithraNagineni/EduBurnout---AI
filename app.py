import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ← CHANGE THIS LINE
client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
db = client["StudentsDB"]