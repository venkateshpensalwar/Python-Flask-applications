from flask import Flask
from flask import render_template, request

app = Flask("AJAX")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sub', methods=['POST'])
def sub():
    name = request.form['name']
    return name
