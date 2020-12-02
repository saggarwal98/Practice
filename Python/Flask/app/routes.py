from app import app,db,models,forms
from flask import render_template,request,Response,json
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
def func():
    fn=open("./app/data/abc.json","r+")
    data=fn.readline()
    data1=json.loads(data)
    print("func")
    return Response(json.dumps(data1),mimetype="application/json")
@app.route("/data_fetch/<idx>")
def data_fetch(idx=None):
    fn=open("./app/data/abc.json","r+")
    data=fn.readline()
    data1=json.loads(data)
    if idx==None:
        return data
    else:
        return Response(json.dumps(data1[int(idx)]),mimetype="application/json")
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

@app.route("/get_user_data")
def get_user_data():
    return render_template("get_user_data.html")
#Save user registration data and send user to homepage
@app.route("/register_user",methods=["POST"])
def register_user():
    user_name=request.form.get("user_name")
    user_email=request.form.get("user_email")
    user_password=request.form.get("user_password")
    u=models.User(user_name=user_name,user_email=user_email,user_password=user_password)
    u.save()
    return "Added user"
#display details all users
@app.route("/get_users")
def get_users():
    users=models.User.objects.all()
    for i in users:
        id=i.user_email
        print(id)
    return render_template("get_users.html",users=users)
# @app.route("/fetch_user_data")
# def fetch_user_data():
#     users=User.objects.all()
#     print(users)
#     # print(users.view_details())
#     return "users[0]"
@app.route("/login_form")
def login_form():
    form=forms.LoginForm()
    return render_template("login_form.html",form=form,login=True)