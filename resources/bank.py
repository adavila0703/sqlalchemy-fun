from flask_restful import Resource
from models.bank import BankModel


class Bank(Resource):
    def get(self, name):
        pass

    def delete(self):
        pass

    def put(self):
        pass


class BankList(Resource):
    pass
