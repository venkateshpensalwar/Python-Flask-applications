from flask import Flask
from flask import request, render_template, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask("Admin_panel")
app.config['SECRET_KEY'] = 'c2Vzc2lvbnM='
app.config['MONGO_URI'] = "mongodb://localhost:27017/digitalstorm"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/')
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('login.html')


@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login():
    ## if session is not going on
    email = request.form['email']
    password = request.form['pass']
    exist = db.users.find_one({'email': email})
    if exist:
        if bcrypt.checkpw(password.encode('utf8'), exist['password']):

           session['email'] = exist['email']
           session['name'] = exist['name']
           session['LoggedIn'] = True
           return 'success'
        else:
           return 'error'
    else:
        return 'Account does Not exist'


@app.route('/dash')
def dash():
    if "LoggedIn" in session:
        bills = db.Bills.find({})
        agg = db.Bills.aggregate(
            [
                {
                    '$group': {
                        '_id': '$category',
                        'total': {
                        '$sum': '$total'
                        }
                    }
                }
        ])
        sum = {}
        for i in agg:
         sum[i['_id']] = i['total']
        return render_template('index.html', bills=bills,total=sum)
    else:
         return redirect('/index')



@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']

    exist = db.users.find_one({
        'email': email
    })
    if exist:
        return "user already exist"
    else:
        if pass1 == pass2:
            hashpass = bcrypt.hashpw(pass1.encode('utf8'), bcrypt.gensalt())
            db.users.insert_one({
                'name': name,
                'email': email,
                'password': hashpass
            })
            return 'success'
        else:
            return "Password should be same"


@app.route('/logout')
def logout():
    session.pop('LoggedIn',None)
    session.pop('name',None)
    session.pop('email',None)
    return render_template('login.html')


@app.route('/Addcash', methods=['POST'])
def Addcash():
   purpose = request.form['purpose']
   total = request.form['money']
   date = request.form['add_date']
   category = 'credit'
   res = {
       'purpose': purpose,
       'total': int(total),
       'date': date,
       'category': category
   }

   db.Bills.insert_one({
       'purpose': purpose,
       'total': int(total),
       'date': date,
       'category': category
   })
   return res


@app.route('/AddExpenses', methods=['POST'])
def AddExpenses():
   purpose = request.form['purpose']
   total = request.form['sum']
   date = request.form['date']
   category = request.form['bill_type']
   res = {
       'purpose': purpose,
       'total': int(total),
       'date': date,
       'category': category
   }
   db.Bills.insert_one({
       'purpose': purpose,
       'total': int(total),
       'date': date,
       'category': category
   })
   return res


app.run(host='127.0.0.1', port=5000)
