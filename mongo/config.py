from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import Flask, jsonify, request, session, redirect
from passlib.hash import sha256_crypt
from functools import wraps
from dotenv import load_dotenv
from pathlib import Path  
import pymongo
import argparse
import uuid
import os


app = Flask(__name__, template_folder="../templates", static_folder='../static')

parser = argparse.ArgumentParser(description='Set up Config File')   
parser = argparse.ArgumentParser()
parser.add_argument('--t', type=str, default="", required= False, help='Template')
parser.add_argument('--c', type=str, default="", required= False, help='Connection string')
parser.add_argument('--s', type=str, default="", required= False, help='Secret Key')

args = parser.parse_args()

load_dotenv()

if  os.environ['SET_UP'] == "False":
    f = open('.env','w')
    val = args.t + ".html" if args.t else False
    f.write('TEMPLATE={}\n'.format(val))
    val_str = args.c if args.c else False
    f.write('MONGO_CONNECTION_STRING={}\n'.format(val_str))
    f.write('SECRET_KEY={}\n'.format(args.s))
    if bool(args.t) and bool(args.c) and bool(args.s):
        f.write('SET_UP=True\n')
    else:
        f.write('SET_UP=False\n')
       
    f.close()


template = os.environ['TEMPLATE']
secret_key = os.environ['SECRET_KEY']
client = pymongo.MongoClient(os.environ['MONGO_CONNECTION_STRING'])
db = client.registration