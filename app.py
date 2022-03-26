import os
import datetime
import random
from flask import (
    Flask, abort, flash, render_template,
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


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if is clock in
        are_in = mongo.db.clocked_in.find_one(
            {"clock_in_nr": request.form.get("clock-number")})
        are_out = mongo.db.clocked_out.find_one(
            {"clock_in_nr": request.form.get("clock-number")})
        employee = mongo.db.employess.find_one(
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
            # Mark clock nr for deletion
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


@app.route("/dashboard/", methods=["GET", "POST"])
def dashboard():
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))
    else:
        admin = list(mongo.db.admin.find())
        username = session["user"]
        return render_template("dashboard.html", username=username, admin=admin)


@app.route("/employess/", methods=["GET", "POST"])
def employess():
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))
    else:
        # List all employee
        employess = list(mongo.db.employess.find())
        return render_template("employess.html", employess=employess)


@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():
    # Check if autontificated
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))

    else:
        # Generating a rondom clock_nr
        rondom_clock_nr = random.randint(1111, 9999)
        check_rondom_clock_nr = mongo.db.employess.find_one(
            {"clock_nr": rondom_clock_nr})

        while check_rondom_clock_nr:
            rondom_clock_nr += 1

        else:
            if request.method == "POST":
                first_name = mongo.db.employess.find_one(
                    {"first_name": request.form.get("first_name").lower()})
                last_name = mongo.db.employess.find_one(
                    {"last_name": request.form.get("last_name").lower()})
                # Check if First Name and Last Name exist already in dayabase to avoid duplicates
                if first_name and last_name:
                    flash(
                        "This persone is already in database please check list of employess")
                    return render_template("add-employee.html")

                else:

                    add_employee = {
                        "first_name": request.form.get("first_name").lower(),
                        "last_name": request.form.get("last_name").lower(),
                        "email": request.form.get("email"),
                        "phone_number": request.form.get("phone_number"),
                        "departament": request.form.get("departament"),
                        "clock_nr": int(request.form.get("clock-in-number")),
                        "start_date": request.form.get("start-date"),
                        "start_time": request.form.get("start-time"),
                        "end_date": request.form.get("end-date"),
                        "end_time": request.form.get("end-time"),
                        "registered_by": session["user"]
                    }
                    # Add new employee to database.
                    mongo.db.employess.insert_one(add_employee)
                    flash("Employee registered successfully")
        return render_template("add-employee.html", clock_nr=rondom_clock_nr)


@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
