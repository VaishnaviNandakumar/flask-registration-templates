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
    
  def register(self):
    form = registerForm(request.form)
    if request.method == 'POST' and form.validate():

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
        error = "Email already exists"
        return render_template('login.html', error = error)

      if db.users.insert_one(user):
        self.start_session(user)
        flash('You are now registered and can log in', 'success')
        return render_template('login.html')

      error = 'Invalid login'
      return render_template('login.html', error=error)
    
    else:
      return render_template('register.html', form = form)


  def logout(self):
    
    session.clear()
    flash("You are now logged out", "success")
    return redirect('/login')
  
  def login(self):
    if request.method == 'POST':
            
      user = db.users.find_one({
        "username" : request.form['username']
      })

      if user and sha256_crypt.verify(request.form['password'], user['password']):
        self.start_session(user)
        return render_template('dashboard.html')

      
      

    return render_template('login.html')
   