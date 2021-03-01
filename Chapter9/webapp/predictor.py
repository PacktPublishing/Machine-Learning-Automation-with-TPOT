import json
import requests


def predict(sepal_length, sepal_width, petal_length, petal_width):
    URL = 'http://ec2-18-220-113-224.us-east-2.compute.amazonaws.com:8000/predict'
    req = requests.post(
        url=URL,
        json={
            'SepalLength': sepal_length,
            'SepalWidth': sepal_width,
            'PetalLength': petal_length,
            'PetalWidth': petal_width
        }
    )
    response = json.loads(req.content)
    return response
