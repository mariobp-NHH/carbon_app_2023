from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
db = SQLAlchemy(application)
db.create_all()

class User(db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    
@application.route('/')
@application.route('/home')
def home():
  return "<h1>Welcome Home</h1>"

if __name__=='__main__':
  application.run(debug=True) 
