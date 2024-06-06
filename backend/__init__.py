from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cftv.db'

db = SQLAlchemy(app)

CORS(app, resources={r"/*":{'origins': 'http//localhost:9000', "allow_headers":
    "Acess-Control-Allow-Origin"}})

from backend import routes
