from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('main.html', name=name)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['value']
    processed_text = text.upper()
    return processed_text