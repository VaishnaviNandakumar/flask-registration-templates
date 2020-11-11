from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

class registerForm(Form):
    name = StringField('Name', [validators.Length(min = 1, max = 50)])
    username = StringField('Username', [validators.Length(min = 4, max = 25)])
    email = StringField('Email', [validators.Length(min = 6, max = 25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods = ['GET','POST'])
def register():
    form = registerForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html', form = form)
    return render_template('register.html', form = form)

if __name__ == "__main__":
    app.run(debug = True)