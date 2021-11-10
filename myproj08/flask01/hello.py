# pip install flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/")
def hello_world():
    return "<p>Hello, hello 백!해!란!!</p>"


@app.route("/profile")
def profile():
    like_foods = ["치킨", "초밥", "샤브샤브", "아메리카노", "버터쿠키"]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
