from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template

app = Flask("Random_quotes")

app.config["MONGO_URI"] = "mongodb://localhost:27017/quots"   ## your db url
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/quote')
def quote():
    res =  db.quot.aggregate([{ "$sample" : { "size" : 1} }])         ## quot is collection name
    return render_template("index.html", res=res)

app.run(port=5000,debug=True)