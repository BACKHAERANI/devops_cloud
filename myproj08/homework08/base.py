from flask import Flask, render_template

app = Flask(__name__)


@app.route("/trip")
def trip():
return render_template("trip.html")