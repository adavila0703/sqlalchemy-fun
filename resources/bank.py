from flask_restful import Resource, reqparse
from models.bank import BankModel


class Bank(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('name',
                       type=str,
                       required=True,
                       help='Name required!'
                       )

    def get(self):
        return BankModel.get_all_banks()

    def post(self):
        data = Bank.parse.parse_args()
        new_bank = BankModel(data['name'])
        new_bank.save_to_db()
        return {'message': 'Bank has been added.'}

    def delete(self):
        pass

    def put(self):
        pass


class BankList(Resource):
    pass
