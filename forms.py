from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TelField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp

class registerForm(FlaskForm):
    name = StringField("Imię", validators=[DataRequired(message="To pole jest wymagane.")])
    email = StringField("Email", validators=[DataRequired(message="Podaj poprawny adres email."), Email()])
    age = IntegerField("Wiek", validators=[DataRequired(message="Podaj wiek między 18 a 100 lat."), NumberRange(min=18, max=100, message="Podaj wiek między 18 a 100 lat.")])
    phone = TelField(
        "Numer telefonu", 
        validators=[
            DataRequired(message="Podaj poprawny numer telefonu."), 
            Regexp("[0-9]{3}-[0-9]{3}-[0-9]{3}", message="Podaj poprawny numer telefonu.")
        ],
        render_kw={
            "aria-describedby": "phoneHelpBlock"
        }
    )
    submit = SubmitField("Wyślij")