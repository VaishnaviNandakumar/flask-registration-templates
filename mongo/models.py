from flask import Flask, jsonify, request, session, redirect
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from registerClass import registerForm
from passlib.hash import sha256_crypt
import app
import pymongo
import uuid

client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    form = registerForm(request.form)
    if request.method == 'POST' and form.validate():
      print(request.form)

      # Create the user object
      user = {
        "_id": uuid.uuid4().hex,
        "name" : form.name.data,
        "email" : form.email.data,
        "username" : form.username.data,
        "password" :  form.password.data

      }

      # Encrypt the password
      user['password'] = sha256_crypt.encrypt(user['password'])


      # Check for existing email address
      if db.users.find_one({ "email": user['email'] }):
        return jsonify({ "error": "Email address already in use" }), 400

      if db.users.insert_one(user):
        return self.start_session(user)

      return jsonify({ "error": "Signup failed" }), 400
    
    else:
      return render_template('register.html', form = form)


  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):
    if request.method == 'POST':
            
      user = db.users.find_one({
        "username" : request.form['username']
      })

      if user and sha256_crypt.verify(request.form['password'], user['password']):
        return self.start_session(user)
      
      #return jsonify({ "error": "Invalid login credentials" }), 401

    return render_template('login.html')
   