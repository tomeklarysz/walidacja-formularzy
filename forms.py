from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TelField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp

class registerForm(FlaskForm):
    name = StringField("Imię", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    age = IntegerField("Wiek", validators=[DataRequired(), NumberRange(min=18, max=100)])
    phone = TelField("Numer telefonu", validators=[DataRequired(), Regexp("[0-9]{3}-[0-9]{3}-[0-9]{3}")])
    submit = SubmitField("Wyślij")