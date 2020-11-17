from config import *
from registerClass import registerForm


class User:
    def register(self):
        form = registerForm(request.form)
        if request.method == 'POST' and form.validate():
            name = form.name.data
            email = form.email.data
            username = form.username.data
            password =  sha256_crypt.encrypt(str(form.password.data))

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
            mysql.connection.commit()
            cur.close()

            flash('You are now registered and can log in', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form = form)

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password_candidate = request.form['password']
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
            if result > 0:
                data = cur.fetchone()
                password = data['password']
                if sha256_crypt.verify(password_candidate, password):
                    session['logged_in'] = True
                    session['username'] = username
                    flash('You are now logged in', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    error = 'Invalid login'
                    return render_template('login.html', error=error)
                cur.close()
            else:
                error = 'Username not found'
                return render_template('login.html', error=error)

        return render_template('login.html')
        
    def logout(self):
        session.clear()
        flash("You are now logged out", "success")
        return render_template('login.html')
    
