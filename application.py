from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__) 

# DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
# db = SQLAlchemy(application)

# class User(db.Model):
#   __tablename__ = "user_table"
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(30), unique=True, nullable=False)
    
@application.route('/')
@application.route('/home')
def home():
#   db.create_all()
#   from application import User
#   user1=User(username='Bjørk')
#   db.session.add(user1)
#   user2=User(username='Fjell')
#   db.session.add(user2)
#   user3=User(username='Regn')
#   db.session.add(user3)
#   user4=User(username='Brann')
#   db.session.add(user4)
#   db.session.commit()
    return "<h1>Welcome Home</h1>"

if __name__=='__main__':
  application.run(debug=True) 
