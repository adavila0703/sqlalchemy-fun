from flask_restful import Resource, reqparse
import sqlite3
from models.user import UserModel


class User(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('username',
                       type=str,
                       required=True,
                       help='username needed'
                       )
    parse.add_argument('money',
                       type=int,
                       required=True,
                       help='money needed'
                       )

    def get(self):
        return UserModel.get_all_users()

    def post(self):

        data = User.parse.parse_args()

        if UserModel.find_user(data['username']):
            return {'message': 'user is already created'}
        else:
            new_user = UserModel(data['username'], data['money'])
            new_user.save_to_db()
            return {'message': 'user added!'}

    def delete(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',
                           type=str,
                           required=True,
                           help='username needed'
                           )
        data = parse.parse_args()
        user = UserModel.find_user(data['username'])
        print(user)
        return {'message': 'Person deleted'}

    def put(self):
        pass


class Test(Resource):
    def get(self, username):
        convert = UserModel.find_user(username)
        return {'username': convert[0], 'money': convert[1]}