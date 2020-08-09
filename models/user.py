from db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    money = db.Column(db.Integer)

    def __init__(self, id, username, money):
        self.id = id
        self.username = username
        self.money = money