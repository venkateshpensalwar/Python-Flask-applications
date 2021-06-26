from flask import Flask
from flask import render_template
import requests

app = Flask('DockerApp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images')
def images():
    Response = requests.get('http://192.168.0.110:2375/images/json')
    return render_template('image.html',images=Response.json())

@app.route('/containers')
def container():
    Response = requests.get(
        'http://192.168.0.110:2375/containers/json?all=true')
    return render_template('containers.html',containers=Response.json())


