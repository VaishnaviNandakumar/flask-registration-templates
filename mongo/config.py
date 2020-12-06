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
    f.write('SET_UP=True\n')
    f.write('TEMPLATE = {}\n'.format(args.t + ".html"))
    f.write('MONGO_CONNECTION_STRING = {}\n'.format(args.c))
    f.write('SECRET_KEY = {}'.format(args.s))
    f.close()

template = os.environ['TEMPLATE']
secret_key = os.environ['SECRET_KEY']
client = pymongo.MongoClient(os.environ['MONGO_CONNECTION_STRING'])
db = client.registration