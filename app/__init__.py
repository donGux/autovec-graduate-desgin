from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

# from config import Config

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY']='rhino'


HostName = "127.0.0.1"
Port = 3306  # 默认为3306，需要自行修改
UserName = "root"  # 默认用户名
Password = "123456"
DataBase = "book"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@127.0.0.1:3306/book"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    UserID = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.String(50))
    Location = db.Column(db.String(50))

# 定义 Book 模型
class Book(db.Model):
    __tablename__ = 'chinese-books'
    BookID = db.Column(db.Integer, primary_key=True)
    书名 = db.Column(db.String(80), nullable=False)
    作者 = db.Column(db.String(80), nullable=False)
    出版社 = db.Column(db.String(20), nullable=False)

from app import routes



#set FLASK_ENV=development
#调试模式






