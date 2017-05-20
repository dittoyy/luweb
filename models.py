#coding:utf-8
from exts import db

class UserModel(db.Model):
    """docstring for UserModel"""
    __tablename__='user'#user is tablename
    id=db.Column(db.Iterger(11),nullable=True,autoincrement=True)
    #Column fieldname
    username=db.Column(db.string(100),nullable=True)
    password=db.Column(db.string(100),nullable=True)
    telephone=db.Column(db.string(100),nullable=True)