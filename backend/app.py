#.\venv\Scripts\activate.bat
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cftv.db'

db = SQLAlchemy(app)

CORS(app, resources={r"/*":{'origins': 'http//localhost:8080', "allow_headers":
    "Acess-Control-Allow-Origin"}})

@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, World!!!!"


if __name__ == '__main__':
    app.run(debug=True)
    
    