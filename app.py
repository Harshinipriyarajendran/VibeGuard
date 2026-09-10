from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/configuration/<vendor>")
def configuration(vendor):
    return render_template("configuration.html", vendor=vendor)


if __name__ == "__main__":
    app.run(debug=True)