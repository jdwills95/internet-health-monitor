from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class AllPingData(Resource):
    @staticmethod
    def get():
        data = pd.read_csv('users.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {"data": data}, 200  # return data and 200 OK code
    pass


api.add_resource(AllPingData, '/all-ping-data')  # '/users' is our entry point

if __name__ == '__main__':
    app.run()  # run our Flask app
