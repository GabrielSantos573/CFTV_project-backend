from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cftv.db'
app.config['SECRET_KEY'] = '99d83fddcdd9f2847cb5faa20a2842dd'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

CORS(app, resources={r"/*":{'origins': 'http//localhost:9000', "allow_headers":
    "Acess-Control-Allow-Origin"}})

from backend import routes
