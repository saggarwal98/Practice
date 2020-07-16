import flask
app=flask.Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    return "<h1>Index Page!</h1>"