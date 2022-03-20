import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, send_from_directory)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if is clock in
        are_in = mongo.db.clocked_in.find_one(
            {"clock_in_nr": request.form.get("clock-number")})
        are_out = mongo.db.clocked_out.find_one(
            {"clock_in_nr": request.form.get("clock-number")})
        employee = mongo.db.employees.find_one(
            {"clock_nr": request.form.get("clock-number")})

        if not employee:
            # Check if clock in number exist in employees
            flash("Your clock number is wrong")
            return render_template("index.html")

        elif are_in:
            # Clock out if is clock in already
            flash(str(employee["first_name"]) + " " + str(employee["last_name"]
                                                          ) + ", " + "you was clock out successfully!")
            clock_out = {
                "clock_in_nr": request.form.get("clock-number"),
                "date": datetime.datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }
            #Insert in clocked_out
            mongo.db.clocked_out.insert_one(clock_out)
            #Mark clock nr for deletion
            clocks = {
                "first_name": employee["first_name"],
                "last_name": employee["last_name"],
                "clock_nr": request.form.get("clock-number"),
                "date_in": are_in["date"],
                "time_in": are_in["time"],
                "date": datetime.datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }
            mongo.db.clocks.insert_one(clocks)
            clock_in = {
                "clock_in_nr": request.form.get("clock-number")
            }
            # Delete from clocked_in
            mongo.db.clocked_in.delete_one(clock_in)

        else:
            # Clock in  if is clock out
            flash(str(employee["first_name"]) + " " + str(employee["last_name"]
                                                          ) + ", " + "you was clock in successfully!")
            clock_in = {
                "clock_in_nr": request.form.get("clock-number"),
                "date": datetime.datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }
            mongo.db.clocked_in.insert_one(clock_in)
            clock_out = {
                "clock_in_nr": request.form.get("clock-number")
            }
            mongo.db.clocked_out.delete_one(clock_out)

    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='img/favicon.ico')


@app.route("/employees")
def employess():
    employees = mongo.db.employess.find_one()
    return render_template("employees.html", employees=employees)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.admin.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "phone_number": request.form.get("phone_number").lower()
        }
        mongo.db.admin.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("dashboard", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.admin.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "dashboard", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    # grab the session user's username from db
    username = mongo.db.admin.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("dashboard.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
