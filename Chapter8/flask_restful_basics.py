from flask import Flask, request, jsonify
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)


class Adding(Resource):
    @staticmethod
    def get():
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return num1 + num2

    @staticmethod
    def post():
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        return jsonify({'result': num1 + num2})

api.add_resource(Adding, '/adding')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)