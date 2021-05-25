# Python-Flask-applications

### To use This applications you need following packages installed
1. python and pip
2. Flask
3. PyMongo

After installing python from offical site you will get pip and using it you need to install last two packages

```
pip install Flask

pip install Flask-pymongo
```

there are two types of enviorment in Flask `Production` and `Development` so you need to choose one of them
according to your requirement

using following command you can set your enviorment

```
for windows
set FLASK_ENV = Development or production

```

```
for linux
export FLASK_ENV = Development or production

```

After that you can run Flask web app using 2 ways

```
flask run
```

```
following line is last line of your app.py file
app.run(port="your number",Debug="true or false",host="ip")

python app.py
```