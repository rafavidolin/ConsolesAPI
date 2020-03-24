from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database\\application.db'
db = SQLAlchemy(app)
api = Api(app)

from my_app.console.views import console
app.register_blueprint(console)

db.create_all()