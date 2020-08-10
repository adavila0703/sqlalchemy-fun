from db import db


class BankModel(db.Model):
    __tablename__ = 'banks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    user = db.relationship('UserModel', backref='owner')

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all_banks(cls):
        templist = []
        for c in cls.query.all():
            tempdict = {'id': c.id, 'name': c.name}
            templist.append(tempdict)
        return templist

    @classmethod
    def get_bank(cls, name):
        print(cls.query.filter_by(name=name).first())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
