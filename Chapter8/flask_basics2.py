from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/adding')
def adding_get():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return f'<h3>{num1} + {num2} = {num1 + num2}</h3>'


@app.route('/adding', methods=['POST'])
def adding_post():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    return jsonify({'result': num1 + num2})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
