from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired


class IrisForm(FlaskForm):
    sepal_length = FloatField(
        label='Sepal Length', validators=[DataRequired()]
    )
    sepal_width = FloatField(
        label='Sepal Width', validators=[DataRequired()]
    )
    petal_length = FloatField(
        label='Petal Length', validators=[DataRequired()]
    )
    petal_width = FloatField(
        label='Petal Width', validators=[DataRequired()]
    )
    submit = SubmitField(label='Predict')
