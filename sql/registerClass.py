from config import *

class registerForm(Form):
    name = StringField('Name', [validators.Length(min = 1, max = 50)])
    username = StringField('Username', [validators.Length(min = 4, max = 25)])
    email = StringField('Email', [validators.Length(min = 6, max = 25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
    ])
    confirm = PasswordField('Confirm Password')


class loginForm(Form):
    
    username = StringField('', render_kw={"placeholder": "Username"})
    password = PasswordField('', [
        validators.DataRequired()
    ], render_kw={"placeholder": "Password"})
    submit2 = SubmitField('Login')