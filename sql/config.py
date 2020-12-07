from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from functools import wraps
import argparse
import hashlib
import os


app = Flask(__name__, template_folder="../templates", static_folder='../static')

parser = argparse.ArgumentParser(description='Set up Config')   
parser = argparse.ArgumentParser()
parser.add_argument('--t', type=str, default="", required= False, help='Template to be used')
parser.add_argument('--h', type=str, default="", required= False, help='MYSQL Host')
parser.add_argument('--u', type=str, default="", required= False, help='MYSQL Username')
parser.add_argument('--p', type=str, default="", required= False, help='MYSQL Password')
parser.add_argument('--db', type=str, default="", required= False, help='Database name')
parser.add_argument('--s', type=str, default="", required= False, help='Secret Key')
args = parser.parse_args()

load_dotenv()

if  os.environ['SET_UP'] == "False":
    f = open('.env','w')
    val = args.t + ".html" if args.t else False
    f.write('TEMPLATE={}\n'.format(val))
    f.write('SQL_HOST= {}\n'.format(args.h))
    f.write('SQL_USERNAME = {}\n'.format(args.u))
    f.write('SQL_PASSWORD = {}\n'.format(args.p))
    f.write('SQL_DB_NAME = {}\n'.format(args.db))
    f.write('SECRET_KEY = {}\n'.format(args.s))
    if bool(args.t) and bool(args.h) and bool(args.u) and bool(args.p) and bool(args.db) and bool(args.s):
        f.write('SET_UP=True\n')
    else:
        f.write('SET_UP=False\n')
       
    f.close()

template = os.environ['TEMPLATE']
secret_key = os.environ['SECRET_KEY']

# Config MySQL
app.config['MYSQL_HOST'] = os.environ['SQL_HOST']
app.config['MYSQL_USER'] =  os.environ['SQL_USERNAME']
app.config['MYSQL_PASSWORD'] = os.environ['SQL_PASSWORD']
app.config['MYSQL_DB'] = os.environ['SQL_DB_NAME']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

    

