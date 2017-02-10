import os
import sys

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

@app.route('/')
def index():
    return '<p>Welcome</p>'


#This will return list of bus times given a stop code
class RunCasper(Resource):
    def get(self, username, password):
        os.system("time python run.py %s %s" % (username, password))

        return {
            "username": username,
            "password": password
        }

        return {"message": "success!"}

api.add_resource(RunCasper, '/runscript/<string:username>/<string:password>')

if __name__ == '__main__':
    app.run(debug=True)
