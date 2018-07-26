from flask import Flask

# Create flask application
app = Flask(__name__)

from app import routes
