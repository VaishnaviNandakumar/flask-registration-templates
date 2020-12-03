from config import *
import argparse
from functools import wraps
from userClass import User



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
  
@app.route('/register', methods = ['GET','POST'])
def register():
    return User().register()

@app.route('/login' , methods = ['GET', 'POST'])
def login():
    return User().login()

@app.route('/logout')
def logout():
    return User().logout()

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.secret_key = 'secret_key123'
    app.run(debug = True)