from config import *
from registerClass import registerForm,loginForm


class User:
  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    
  def register(self):
    reg_form = registerForm(request.form)
    login_form = loginForm(request.form)

    if request.method == "POST":   
      #Registration Form
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
          error = "Email already exists!"
          return render_template(template, error = error, reg_form=reg_form, login_form=login_form)
        
        if db.users.insert_one(user):
          self.start_session(user)
          flash('You are now registered and can log in!', 'success')
          return render_template(template,  reg_form=reg_form, login_form=login_form) 
      
      #Login Form
      elif login_form.submit2.data and login_form.validate(): 
        user = db.users.find_one({
         "username" : login_form.username.data })

        if user:
          if sha256_crypt.verify(login_form.password.data, user['password']):
            self.start_session(user)
            return render_template('dashboard.html')
          else:
            error = 'Incorrect login details!'
            return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)
        else:
            error = 'Username not found!'
            return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)
      
      error = 'Check the registered details!'
      return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)
  
    else:
      try:
        return render_template(template, reg_form=reg_form, login_form=login_form)
      except Exception as e:
        return "Given template does not exists."

  def logout(self):
    session.clear()
    flash("You are now logged out!", "success")
    return redirect('/')
  
     

  
   