from datetime import datetime
from capp import application, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Database User
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    chats_gender = db.relationship('ChatGender', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Database Gender Platform
class ChatGender(db.Model):
    __bind_key__ = 'gender_platform'
    __tablename__ = 'chat_gender'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatGender('{self.title}')"
