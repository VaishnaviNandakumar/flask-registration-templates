from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators,  SubmitField
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import hashlib


class registerForm(Form):
    name = StringField('', [ validators.DataRequired(),validators.Length(min = 1, max = 50)], render_kw={"placeholder": "Name"})
    username = StringField('', [validators.Length(min = 4, max = 25)], render_kw={"placeholder": "Username"})
    email = StringField('', [validators.Length(min = 6, max = 25)], render_kw={"placeholder": "Email"})
    password = PasswordField('', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match!")
    ], render_kw={"placeholder": "Password"})
    confirm = PasswordField('', render_kw={"placeholder": "Confirm Password"})
    submit1 = SubmitField('Register')


class loginForm(Form):
    
    username = StringField('', render_kw={"placeholder": "Username"})
    password = PasswordField('', [
        validators.DataRequired()
    ], render_kw={"placeholder": "Password"})
    submit2 = SubmitField('Login')