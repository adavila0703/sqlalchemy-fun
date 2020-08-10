from flask import Flask
from flask_restful import Api
from resources.user import User, Test
from resources.bank import Bank, BankList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bankdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Bank, '/bank')
api.add_resource(User, '/user')
api.add_resource(Test, '/test/<string:username>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
