from flask import Flask
from flask_restful import Api, Resource, reqparse
from create_tables import maketable
import sqlite3
from resources.resources import Bank, User

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(Bank, '/bank')
api.add_resource(User, '/user')

maketable()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
