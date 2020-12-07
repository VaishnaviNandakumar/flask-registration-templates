from config import *
from registerClass import registerForm, loginForm


class User:
    
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user

    def register(self):
        reg_form = registerForm(request.form)
        login_form = loginForm(request.form)

        #Registration Form
        if request.method == 'POST' :
            try:
                cur = mysql.connection.cursor()
            except Exception as e:
                return "Access Denied. Check your MYSQL Username/Password."

            if reg_form.submit1.data and reg_form.validate():
                name = reg_form.name.data,
                email = reg_form.email.data,
                username = reg_form.username.data,
                password = sha256_crypt.encrypt(reg_form.password.data)
                
                
                mail = cur.execute("SELECT * FROM users WHERE email = %s", [email])
                if mail>0:
                    error = "Email already exists!"
                    return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)

                cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name , email, username, password))
                mysql.connection.commit()
                result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
                data = cur.fetchone()
                self.start_session(data)
                cur.close()
                flash('You are now registered and can log in!', 'success')
                return render_template(template,  reg_form=reg_form, login_form=login_form) 
            
            #Login Form
            elif login_form.submit2.data and login_form.validate(): 
                username = login_form.username.data
                password_candidate = login_form.password.data
                result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
                if result > 0:
                    data = cur.fetchone()
                    password = data['password']
                    if sha256_crypt.verify(password_candidate, password):
                        self.start_session(data)
                        return redirect(url_for('dashboard'))
                    else:
                        error = 'Incorrect login details!'
                        return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)
                    cur.close()
                else:
                    error = 'Username not found!'
                    return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)
            
            error = 'Check the registered details!'
            return render_template(template, error=error,  reg_form=reg_form, login_form=login_form)
        
        
        try:
            return render_template(template, reg_form=reg_form, login_form=login_form)
        except Exception as e:
            if not cnf_setup:
                return "Set up config file."
            else:
                return "Given template does not exists."
            
       
        
    def logout(self):
        session.clear()
        flash("You are now logged out!", "success")
        return redirect('/')
    
