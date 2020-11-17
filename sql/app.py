from config import *
from functools import wraps
from userClass import User


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