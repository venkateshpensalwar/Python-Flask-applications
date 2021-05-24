
from flask import Flask
from flask import render_template,request
from flask_pymongo import  PyMongo
from flask import redirect


app = Flask("CURD_APP")
app.config['MONGO_URI'] = "mongodb://127.0.0.1:27017/CURD"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/insert",methods=['POST'])
def insert():
       name = request.form.get('Fname')
       mobile = request.form.get('mobile')
       address = request.form.get('address')
       comment = request.form.get('comment')

       db.student_details.insert_one(
              {
                     'name': name,
                     'mobile': mobile,
                     'address': address,
                     'comment': comment
              }
       )
       return redirect("/show")

@app.route("/show")
def show():
       student = db.student_details.find({})
       return render_template("show.html",details=student)

@app.route("/update/<ObjectId:id>")
def update(id):
    student = db.student_details.find_one({ "_id": id})
    return render_template("update.html", details=student)

@app.route("/update_record/<ObjectId:id>",methods=["POST"])
def update_record(id):

    name = request.form.get('Fname')
    mobile = request.form.get('mobile')
    address = request.form.get('address')
    comment = request.form.get('comment')

    db.student_details.update_one(
            {"_id": id},
           {'$set':
                   {
                            'name': name,
                            'mobile': mobile,
                            'address': address,
                            'comment': comment
                   }
          })

    return redirect('/show')



@app.route("/delete/<ObjectId:id>")
def delete(id):
       db.student_details.delete_one(
              {"_id": id}
       )
       return redirect("/show")


@app.errorhandler(404)
def error_404(e):
       return render_template('404.html')

app.run(port=5000,debug=True)