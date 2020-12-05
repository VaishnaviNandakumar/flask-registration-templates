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
parser.add_argument('--u', type=str, default="", required= True, help='MYSQL Username')
parser.add_argument('--p', type=str, default="", required= True, help='MYSQL Password')
parser.add_argument('--db', type=str, default="", required= True, help='Database name')


args = parser.parse_args()
template = args.t + ".html"

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] =  args.u
app.config['MYSQL_PASSWORD'] = args.p
app.config['MYSQL_DB'] = args.db
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
