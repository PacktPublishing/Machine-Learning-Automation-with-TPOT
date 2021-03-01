import numpy as np
from flask import Flask, render_template
from forms import IrisForm
from predictor import predict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'


@app.route('/', methods=['GET', 'POST'])
def index():
    iris_form = IrisForm()
    if iris_form.validate_on_submit():
        pred_response = predict(
            sepal_length=iris_form.sepal_length.data,
            sepal_width=iris_form.sepal_width.data,
            petal_length=iris_form.petal_length.data,
            petal_width=iris_form.petal_width.data
        )
        return render_template(
            'predicted.html',
            sepal_length=pred_response['In_PetalLength'],
            sepal_width=pred_response['In_PetalWidth'],
            petal_length=pred_response['In_SepalLength'],
            petal_width=pred_response['In_SepalWidth'],
            prediction=pred_response['Prediction'],
            probability=f"{np.round((pred_response['Probability'] * 100), 2)}%"
        )
    return render_template('index.html', iris_form=iris_form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9500)