from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import hashlib
from functools import wraps

app = Flask(__name__)


# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_DB'] = 'registration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('login.html')


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
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = hashlib.md5((str(form.password.data)).encode())
        
        cur = mysql.connection.cursor()
        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        mysql.connection.commit()
        cur.close()

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

if __name__ == "__main__":
    app.secret_key = 'secret_key123'
    app.run(debug = True)