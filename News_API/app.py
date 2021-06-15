## NewsApi is used for This project 
from flask import Flask
from flask import render_template, request
import requests as req
import config

app = Flask("News_api")

@app.route('/')
@app.route('/index')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&pageSize=10&apiKey={}".format(
        config.API_KEY)
    Response = req.get(url)
    TopNews = Response.json()
    return render_template("index.html", News=TopNews)

@app.route('/business')
def business():
        url = "https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=10&apiKey={}".format(
        config.API_KEY)
        Response = req.get(url)
        TopNews = Response.json()
        return render_template("business.html", News=TopNews, num=len(TopNews['articles']))


@app.route('/entertainment')
def entertainment():
    url = "https://newsapi.org/v2/top-headlines?category=entertainment&pageSize=10&apiKey={}".format(
        config.API_KEY)
    Response = req.get(url)
    TopNews = Response.json()
    return render_template("entertainment.html", News=TopNews, num=len(TopNews['articles']))

@app.route('/general')
def general():
    url = "https://newsapi.org/v2/top-headlines?category=general&pageSize=10&apiKey={}".format(
        config.API_KEY)
    Response = req.get(url)
    TopNews = Response.json()
    return render_template("general.html", News=TopNews, num=len(TopNews['articles']))

@app.route('/health')
def health():
    url = "https://newsapi.org/v2/top-headlines?category=health&pageSize=10&apiKey={}".format(
        config.API_KEY)
    Response = req.get(url)
    TopNews = Response.json()
    return render_template("health.html", News=TopNews, num=len(TopNews['articles']))

@app.route('/science')
def science():
    url = "https://newsapi.org/v2/top-headlines?category=science&pageSize=10&apiKey={}".format(
        config.API_KEY)
    Response = req.get(url)
    TopNews = Response.json()
    return render_template("science.html", News=TopNews, num=len(TopNews['articles']))

@app.route('/technology')
def technology():
    url = "https://newsapi.org/v2/top-headlines?category=technology&pageSize=10&apiKey={}".format(
        config.API_KEY)
    Response = req.get(url)
    TopNews = Response.json()
    return render_template("technology.html", News=TopNews, num=len(TopNews['articles']))
