from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators,  SubmitField
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import hashlib


class registerForm(Form):
    name = StringField('Name', [ validators.DataRequired(),validators.Length(min = 1, max = 50)])
    username = StringField('Username', [validators.Length(min = 4, max = 25)])
    email = StringField('Email', [validators.Length(min = 6, max = 25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
    ])
    confirm = PasswordField('Confirm Password')
    submit1 = SubmitField('Register')


class loginForm(Form):
    
    username = StringField('Username')
    password = PasswordField('Password', [
        validators.DataRequired()
    ])
    submit2 = SubmitField('Login')