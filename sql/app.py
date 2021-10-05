from config import *
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
    app.secret_key = secret_key
    app.run()
