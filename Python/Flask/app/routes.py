from app import app
from flask import render_template,request
import os
#default routes
@app.route("/")
@app.route("/index")
@app.route("/index/<year>")
def index(year=2020):
    return render_template("index.html",login=True,year=year)
#route for about page
@app.route("/about")
def about():
    return render_template("about.html")
#route for services page
@app.route("/services")
def services():
    return render_template("services.html")
#route for contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")
#route for internal fetching data from json file
@app.route("/data_fetch")
def data_fetch():
    fn=open("./app/data/abc.json","r+")
    data=fn.readline()
    return data
#route for displaying data from json file into table
@app.route("/data")
def data():
    return render_template("data.html")
#route for register form with get method
@app.route("/register_get")
def register_get():
    return render_template("register_get.html")
#route for register form with post method
@app.route("/register_post")
def register_post():
    return render_template("register_post.html")
#route for displaying register data received from get method
@app.route("/register_data_get",methods=["GET"])
def register_data_get():
    name=request.args.get("name")
    age=request.args.get("age")
    gender=request.args.get("gender")
    return render_template("register_data.html",data={"name":name,"age":age,"gender":gender})
#route for displaying register data received from post method
@app.route("/register_data_post",methods=["POST"])
def register_data_post():
    name=request.form.get("name")
    age=request.form.get("age")
    gender=request.form.get("gender")
    return render_template("register_data.html",data={"name":name,"age":age,"gender":gender})
#if want to display data in json format use json.dumps(data),mimetype="application/json" within Response function and import Response and json from flask