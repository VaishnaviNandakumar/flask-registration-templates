from flask import Flask, jsonify, request, session, redirect
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from registerClass import registerForm,loginForm
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
    reg_form = registerForm(request.form)
    login_form = loginForm(request.form)
    if request.method == "POST":   
      if reg_form.submit1.data and reg_form.validate():
        user = {
          "_id": uuid.uuid4().hex,
          "name" : reg_form.name.data,
          "email" : reg_form.email.data,
          "username" : reg_form.username.data,
          "password" :  reg_form.password.data
        }
        user['password'] = sha256_crypt.encrypt(user['password'])
        if db.users.find_one({ "email": user['email'] }):
          error = "Email already exists"
          return render_template('login.html', error = error, reg_form=reg_form, login_form=login_form)
        

        if db.users.insert_one(user):
          self.start_session(user)
          flash('You are now registered and can log in', 'success')
          return render_template('register.html',  reg_form=reg_form, login_form=login_form)
    
      
      
      elif login_form.submit2.data and login_form.validate(): 
        user = db.users.find_one({
         "username" : login_form.username.data })

        if user and sha256_crypt.verify(login_form.password.data, user['password']):
          self.start_session(user)
          return render_template('dashboard.html')


      error = 'Check details!'
      return render_template('register.html', error=error,  reg_form=reg_form, login_form=login_form)
  
    else:
      return render_template('register.html', reg_form=reg_form, login_form=login_form)

  def logout(self):
    
    session.clear()
    flash("You are now logged out", "success")
    return redirect('/register')
  
     

  
   