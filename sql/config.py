from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import argparse
import hashlib


app = Flask(__name__, template_folder="../templates", static_folder='../static')
parser = argparse.ArgumentParser(description='Set up Config File')   
parser = argparse.ArgumentParser()
parser.add_argument('--t', type=str, default="", required= True, help='Template')
args = parser.parse_args()
if args.t == "template1":
  template = "template1.html"
elif args.t == "template2":
  template = "template2.html"
elif args.t == "template3":
  template = "template3.html"
else:
  print("Template does not exists.")
  
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
