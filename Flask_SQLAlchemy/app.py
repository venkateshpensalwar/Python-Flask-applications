
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask("SQL_APP")


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/test.sqlite"
db = SQLAlchemy(app)
#print(db)

class child(db.Model):
# Creating child class from db.model and creating columns 
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    remarks = db.Column(db.String)

    def __init__(self,name,age,remarks):
        self.name = name
        self.age = age
        self.remarks = remarks

# to create database with all above schemas
db.create_all()

# creating instance for inserting data

jack = child("jack",20,"Good")

## To add this data in database so we need to add with session

db.session.add(jack)

## we need to commit it becuse database is critical
db.session.commit()

## To read the data from database

read = child.query.get(1)
print(read)
print(read.name)

## To read all the data 

readAll = child.query.all()
print(readAll)

## To search in the database

search = child.query.filter_by(age=20)
print(search)

## To update data
update = child.query.get(2)
update.age = 15
db.session.add(update)
db.session.commit()

## To delete the data

delete1 = child.query.get(2)
db.session.delete(delete1)
db.session.commit()
