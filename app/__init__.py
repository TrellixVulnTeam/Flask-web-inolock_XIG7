from crypt import methods
from flask import Flask, render_template
from flask_cors import CORS
from app.configs import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
     return render_template('index.html')


from app.test import test
from app.introduction.product import product

app.register_blueprint(test)
app.register_blueprint(product)