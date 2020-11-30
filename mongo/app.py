from flask import Flask, render_template, session, redirect
from functools import wraps
from user import *
import argparse

app = Flask(__name__)

parser = argparse.ArgumentParser(description='Set up Config File')   
parser = argparse.ArgumentParser()
parser.add_argument('--t', type=str, default="", required= True, help='Template')
args = parser.parse_args()
if args.t == "template1":
  template = "template1.html"
elif args.t == "template2":
  template = "template2.html"
elif args.t == "template3":
  template = "template3.html"
else:
  print("Template does not exists.")


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash('Unauthorized. Please login.', 'danger')
      return redirect('/')
  
  return wrap


@app.route('/', methods=['POST','GET'])
def register():
  return User().register()


@app.route('/logout')
def logout():
  return User().logout()

@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html')

if __name__ == "__main__":
    app.secret_key =  b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
    app.run(debug = True)

