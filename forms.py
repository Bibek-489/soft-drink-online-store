from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo

class SignupForm(FlaskForm):
    
    username = StringField(
        "Username",
        validators = [DataRequired(), Length(4,15)]
    )

    email = StringField(
        "Email",
        validators = [DataRequired(), Email()]
    )

    gender = SelectField(
        "Gender",
        choices = ["male","female","others"],
        validators = [Optional()]
    )

    dob = DateField(
        "Date of Birth",
        validators = [DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators = [DataRequired(), Length(5,15)]
    )

    confirmPassword = PasswordField(
        "ConfirmPassword",
        validators = [DataRequired(), Length(5,15), EqualTo("password")]
    )

    submit = SubmitField(
        "Submit"
    )

class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators = [DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators = [DataRequired(), Length(5,15)]
    )

    remeberme = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Log in"
    )