from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    money = db.Column(db.Integer)

    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    banks = db.relationship('BankModel')

    def __init__(self, username, money):
        self.username = username
        self.money = money

    @classmethod
    def find_user(cls, username):
        try:
            return cls.query.filter_by(username=username).first().username, \
                   cls.query.filter_by(username=username).first().money, 200
        except AttributeError:
            return None

    @classmethod
    def get_all_users(cls):
        templist = []
        for c in cls.query.all():
            tempdict = {'username': c.username, 'money': c.money, 'bankid': c.banks}
            templist.append(tempdict)
        return templist

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
