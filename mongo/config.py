from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import Flask, jsonify, request, session, redirect
from passlib.hash import sha256_crypt
from functools import wraps
import pymongo
import argparse
import uuid


app = Flask(__name__, template_folder="../templates", static_folder='../static')

parser = argparse.ArgumentParser(description='Set up Config File')   
parser = argparse.ArgumentParser()
parser.add_argument('--t', type=str, default="", required= True, help='Template')

args = parser.parse_args()
template = args.t + ".html"



client = pymongo.MongoClient('<Connection Strin>')
db = client.registration