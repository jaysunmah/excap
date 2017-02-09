from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
@app.route('/')
def index():
    return '<p>Welcome</p>'


#This will return list of bus times given a stop code
class SetLocation(Resource):
    def get(self, lat, lon):
        global mylat
        global mylon
        mylat = lat
        mylon = lon
        return {
            "lat": mylat,
            "lon": mylon
        }

    def post(self, stop_code):
        print(request.form['data'])
        return {"message": "success!"}

api.add_resource(SetLocation, '/runscript')

if __name__ == '__main__':
    app.run(debug=True)
