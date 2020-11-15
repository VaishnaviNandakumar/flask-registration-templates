from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/login')
  
  return wrap

@app.route('/register')
def home():
  return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html')


