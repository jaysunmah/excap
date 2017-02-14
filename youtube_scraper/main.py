import os
import sys
import check_youtube

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

@app.route('/')
def index():
    return '<p>Welcome</p>'


#This will return list of bus times given a stop code
class RunCasper(Resource):
    def get(self, service, username, password):
        if (service == "youtube"):
            os.system("casperjs youtube_history.js %s %s" % (username, password))
        elif (service == "save_images"):
            os.system("python save_img.py")
        elif  (service == "parse_images"):
            os.system("python parse_images.py %s" % username)
        elif (service == "arrange_files"):
            os.system("mv %s downloaded" % username)
            os.system("mv %s_parsed parsed" % username)
            os.system("mkdir %s" % username)
            os.system("mv downloaded %s" % username)
            os.system("mv parsed %s" % username)
            os.system("python overlay.py %s" % username)
            os.system("cp %s/%s_parsed_stitched.png webserver/public/images" % (username, username))
        elif (service == "check_login"):
            print("Checking youtube account info...")
            os.system("casperjs youtube_verify.js %s %s" % (username, password))
            return check_youtube.checkSuccessLogin()
        # os.system("time python run.py %s %s" % (username, password))

        return {
            "username": username,
            "password": password
        }

        return {"message": "success!"}

api.add_resource(RunCasper, '/runscript/<string:service>/<string:username>/<string:password>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
