import requests

req = requests.post(
    url='http://localhost:8000/adding',
    json={'num1': 3, 'num2': 5}
)
res = req.content

print(res)
