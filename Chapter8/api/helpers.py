def int_to_species(in_species):
    if in_species == 0:
        return 'setosa'
    if in_species == 1:
        return 'virginica'
    if in_species == 2:
        return 'versicolor'


def predict_single(model, X):
    if type(X) is not list:
        raise Exception('X must be of list data type!')
    if len(X) != 4:
        raise Exception('X must contain 4 values - sepal_length, sepal_width, petal_length, petal_width')
    prediction = model.predict([X])[0]
    prediction_probability = model.predict_proba([X])[0][prediction]
    return {
        'In_SepalLength': X[0],
        'In_SepalWidth': X[1],
        'In_PetalLength': X[2],
        'In_PetalWidth': X[3],
        'Prediction': int_to_species(prediction),
        'Probability': prediction_probability
    }
