import os
import json
import requests
from dotenv import load_dotenv
load_dotenv('.env')


def predict(sepal_length, sepal_width, petal_length, petal_width):
    URL = os.getenv('API_ENDPOINT')
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
