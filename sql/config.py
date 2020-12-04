from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import argparse
import hashlib


app = Flask(__name__, template_folder="../templates", static_folder='../static')

parser = argparse.ArgumentParser(description='Set up Config')   
parser = argparse.ArgumentParser()
parser.add_argument('--t', type=str, default="", required= True, help='Template to be used')

args = parser.parse_args()
template = args.t + ".html"

  
  
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
