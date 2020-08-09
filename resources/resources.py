from flask_restful import Resource, reqparse

class User(Resource):
    def post(self):
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

        data = parse.parse_args()

        connection = sqlite3.connect('bankdata.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username=?'
        if cursor.execute(query, (data['username'],)).fetchone():
            connection.close()
            return {'message': 'user is already created'}
        else:
            query = 'INSERT INTO users VALUES (NULL, ?, ?)'
            cursor.execute(query, (data['username'], data['money']))

            connection.commit()
            connection.close()
            return {'message': 'user added!'}


class Bank(Resource):
    def get(self):
        return 'hi'

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',
                           type=str,
                           required=True,
                           help='Requires username'
                           )
        parse.add_argument('money',
                           type=int,
                           required=True,
                           help='Requires money'
                           )
        data = parse.parse_args()

        connection = sqlite3.connect('bankdata.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUE money=? WHERE username=?'

        cursor.execute(query, (data['money'], data['username']))

        connection.commit()
        connection.close()