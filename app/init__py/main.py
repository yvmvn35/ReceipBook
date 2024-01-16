from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#change
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)

from app import routes

