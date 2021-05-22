
from flask import Flask
from flask import render_template
from flask import request


app = Flask("MyApp")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/show", methods=['GET', 'POST'])
def show():
    name = request.form['Name']
    last = request.form['Last']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    return render_template(
        'show.html',
        name=name,
        last=last,
        address=address,
        city=city,
        state=state
    )


app.run(host='0.0.0.0', port=5000, debug=True)
