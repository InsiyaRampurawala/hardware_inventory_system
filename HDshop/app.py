
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/check", methods=["POST"])
def check():
    email = request.form["email"]
    password = request.form["password"]
    print("Email entered:", email)
    print("Password entered:", password)
    if email == 'admin@gmail.com' and password == "admin123":
        return redirect(url_for("enquire"))
    else:
        return "Wrong username or password"

@app.route("/enquire")
def enquire():
    return render_template("enquire.html")

@app.route("/product_list.html")
def product_list():
    return render_template("product_list.html")


if __name__ == "__main__":
    app.run(debug=True)