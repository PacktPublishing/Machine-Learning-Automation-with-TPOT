import joblib 
import warnings
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from helpers import predict_single
warnings.filterwarnings('ignore')

app = Flask(__name__)
api = Api(app)
model = joblib.load('model/iris.model')


class PredictSpecies(Resource):
    @staticmethod
    def post():
        user_input = request.get_json()
        sl = user_input['SepalLength']
        sw = user_input['SepalWidth']
        pl = user_input['PetalLength']
        pw = user_input['PetalWidth']

        prediction = predict_single(model=model, X=[sl, sw, pl, pw])
        return jsonify(prediction)


api.add_resource(PredictSpecies, '/predict')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
