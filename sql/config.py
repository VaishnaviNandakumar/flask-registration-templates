from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import hashlib


app = Flask(__name__, template_folder="../templates", static_folder='../static')
#template = "template1.html"
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'bookworm007'
app.config['MYSQL_DB'] = 'registration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
