from config import *
from functools import wraps
from userClass import User

 
@app.route('/', methods = ['GET','POST'])
def register():
    return User().register()

@app.route('/logout')
def logout():
    return User().logout()

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized. Please login.', 'danger')
            return redirect('/')
    return wrap

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
    app.run(debug = True)