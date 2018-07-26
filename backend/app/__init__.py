from flask import Flask
from flask_cors import CORS
# Create flask application
app = Flask(__name__)
CORS(app)
from app import routes
