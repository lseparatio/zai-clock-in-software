from crypt import methods
import os
import datetime
import random
import re
import uuid
from flask import (
    Flask, Markup, flash, render_template,
    redirect, request, session, url_for, send_from_directory)
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# App dinamic config, do not update, use env instead
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
# Mail dinamic config, do not update, use env instead
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)
mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(e):
    settings = list(mongo.db.index_template.find())
    # note that we set the 404 status explicitly
    return render_template('404.html', settings=settings), 404


@app.route("/", methods=["GET", "POST"])
def index():
    settings = mongo.db.index_template.find()
    if request.method == "POST":
        # Check if is clock in
        are_in = mongo.db.clocked_in.find_one(
            {"clock_in_nr": int(request.form.get("clock-number"))})
        employee = mongo.db.employess.find_one(
            {"clock_nr": int(request.form.get("clock-number"))})

        if not employee:
            # Check if clock in number exist in employees
            flash("Your clock number is wrong")
            return render_template("index.html", settings=settings)

        elif are_in:
            # Clock out if is clock in already
            flash(str(employee["first_name"].capitalize()) + " " + str(employee["last_name"].capitalize()
                                                                       ) + ", " + "you was clock out successfully!")
            clock_out = {
                "clock_in_nr": int(request.form.get("clock-number")),
                "date": datetime.datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }
            # Insert in clocked_out
            mongo.db.clocked_out.insert_one(clock_out)
            # Mark clock nr for deletion
            clocks = {
                "first_name": employee["first_name"],
                "last_name": employee["last_name"],
                "clock_nr": int(request.form.get("clock-number")),
                "date_in": are_in["date"],
                "time_in": are_in["time"],
                "date": datetime.datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }
            mongo.db.clocks.insert_one(clocks)
            clock_in = {
                "clock_in_nr": int(request.form.get("clock-number"))
            }
            # Delete from clocked_in
            mongo.db.clocked_in.delete_one(clock_in)

        else:
            # Clock in  if is clock out
            flash(str(employee["first_name"].capitalize()) + " " + str(employee["last_name"].capitalize()
                                                                       ) + ", " + "you was clock in successfully!")
            clock_in = {
                "clock_in_nr": int(request.form.get("clock-number")),
                "date": datetime.datetime.now().strftime("%m/%d/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }
            mongo.db.clocked_in.insert_one(clock_in)
            clock_out = {
                "clock_in_nr": int(request.form.get("clock-number"))
            }
            mongo.db.clocked_out.delete_one(clock_out)

    return render_template("index.html", settings=settings)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='img/favicon.ico')


@app.route("/register", methods=["GET", "POST"])
def register():
    settings = list(mongo.db.index_template.find())
    if request.method == "POST":
        # check if username or email already exists in db
        existing_user = mongo.db.admin.find_one(
            {"username": request.form.get("username").lower()})
        existing_email = mongo.db.admin.find_one(
            {"email": request.form.get("email").lower()})
        existing_phone = mongo.db.admin.find_one(
            {"phone_number": request.form.get("phone_number")})
        verify_secret = uuid.uuid4()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        elif existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))
        elif existing_phone:
            flash("Phone number already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "email_is_verified": False,
            "verify_secret": str(verify_secret),
            "phone_number": request.form.get("phone_number")
        }
        mongo.db.admin.insert_one(register)

        email = request.form.get("email").lower()
        flash("Registration Successful! Please check your email for secret key!")
        # Sending verification email
        msg = Message(
            'Zai Clocking Software. Please confirm your email!', recipients=[email])
        msg.html = render_template("email/verify.html", first_name=request.form.get("first_name").capitalize(
        ), last_name=request.form.get("last_name").capitalize(), email=request.form.get("email").lower(), secret=str(verify_secret))
        mail.send(msg)
        return redirect(url_for("verify"))

    return render_template("register.html", settings=settings)


@app.route("/verify", methods=["GET", "POST"])
def verify():
    settings = list(mongo.db.index_template.find())
    if request.method == "POST":
        # Check if email exists in db
        existing_email = mongo.db.admin.find_one(
            {"email": request.form.get("email").lower()})
        try:
            # Check if key exist in db
            existing_email_secret = existing_email["verify_secret"]
        except:
            flash("Your verification code is wrong, please try again!")
            return redirect(url_for("verify"))

        if existing_email_secret == request.form.get("secret"):
            # Check if key match
            mongo.db.admin.update_one({"email": request.form.get("email").lower()}, {
                                      "$set": {"email_is_verified": True}})
            mongo.db.admin.update_one({"email": request.form.get("email").lower()}, {
                                      "$unset": {"verify_secret": request.form.get("secret")}})
            flash("Your email is now verified please Log In")
            return redirect(url_for("login"))

        flash("Your verification code is wrong, please try again!")
        return render_template("verify.html", settings=settings)

    return render_template("verify.html", settings=settings)


@app.route("/resend-verification", methods=["GET", "POST"])
def resend_verification():
    settings = list(mongo.db.index_template.find())
    if request.method == "POST":
        existing_email = mongo.db.admin.find_one(
            {"email": request.form.get("email").lower()})
        email = request.form.get("email").lower()

        if not existing_email:
            flash("Please double check your email address!")
            return redirect(url_for("resend_verification"))
        elif existing_email:
            # Sending verification email
            msg = Message(
                'Zai Clocking Software. Please confirm your email!', recipients=[email])
            msg.html = render_template(
                "email/verify.html", first_name=existing_email["first_name"].capitalize(), last_name=existing_email["last_name"].capitalize(), email=existing_email["email"], secret=existing_email["verify_secret"])
            mail.send(msg)
            flash("Your verification secret code was sent to email.")
            return redirect(url_for("verify"))

    return render_template("resend-verification.html", settings=settings)


@app.route("/login", methods=["GET", "POST"])
def login():
    settings = list(mongo.db.index_template.find())
    if request.method == "POST":
        # check if email exists in db
        existing_user = mongo.db.admin.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            if not (existing_user["email_is_verified"]):
                # Check id email is verified
                flash(
                    "You need to verify your email address please check your email for instructions")
                return redirect(url_for("verify"))
            # ensure hashed password matches user input
            elif check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Welcome, {}".format(
                    request.form.get("email")))
                return redirect(url_for(
                    "dashboard", email=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", settings=settings)


@app.route("/dashboard/", methods=["GET", "POST"])
def dashboard():
    settings = list(mongo.db.index_template.find())
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))

    email = session["user"]
    admin = mongo.db.admin.find({"email": session["user"]})
    return render_template("dashboard.html", email=email, admin=admin, settings=settings)


@app.route("/employess/", methods=["GET", "POST"])
def employess():
    settings = list(mongo.db.index_template.find())
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))

    # List all employee
    employess = list(mongo.db.employess.find())
    return render_template("employess.html", employess=employess, settings=settings)


@app.route("/search", methods=["GET", "POST"])
def search():
    settings = list(mongo.db.index_template.find())
    try:
        # Managing direct link access
        query = request.form.get("query")
        employess = list(mongo.db.employess.find(
            {"$text": {"$search": query}}))
        if 'user' not in session:
            # Check if is authenticated
            flash("You need to be authenticated to access this page!")
            return redirect(url_for("login"))

        else:
            if employess == []:
                flash("No employee found. Please check again your search parameter")
                return render_template("employess.html", employess=employess, settings=settings)

            return render_template("employess.html", employess=employess, settings=settings)
    except:
        flash("Something wrong happen please try again")
        return redirect(url_for("employess"))


@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():
    settings = list(mongo.db.index_template.find())
    # Check if autentificated
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
                    return render_template("add-employee.html", settings=settings)

                else:

                    add_employee = {
                        "first_name": request.form.get("first_name").lower(),
                        "last_name": request.form.get("last_name").lower(),
                        "email": request.form.get("email").lower(),
                        "phone_number": request.form.get("phone_number"),
                        "departament": request.form.get("departament").lower(),
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

        return render_template("add-employee.html", clock_nr=rondom_clock_nr, settings=settings)


@app.route("/edit_employee/<clock_number>", methods=["GET", "POST"])
def edit_employee(clock_number):
    settings = list(mongo.db.index_template.find())
    employess = mongo.db.employess.find_one({"clock_nr": int(clock_number)})
    # Check if autentificated
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))
    elif request.method == "POST":
        mongo.db.employess.update_one({"clock_nr": int(clock_number)}, {"$set":
                                                                        {"first_name": request.form.get("first_name").lower(),
                                                                         "last_name": request.form.get("last_name").lower(),
                                                                         "email": request.form.get("email").lower(),
                                                                         "phone_number": request.form.get("phone_number"),
                                                                         "departament": request.form.get("departament").lower(),
                                                                         "clock_nr": int(request.form.get("clock-in-number")),
                                                                         "start_date": request.form.get("start-date"),
                                                                         "start_time": request.form.get("start-time"),
                                                                         "end_date": request.form.get("end-date"),
                                                                         "end_time": request.form.get("end-time"),
                                                                         "registered_by": employess["registered_by"],
                                                                         "last_updated_by": session["user"]}})
        flash("Employee Successfully Updated")
        return redirect(url_for("edit_employee", clock_number=clock_number))

    else:
        return render_template("edit-employee.html", employess=employess, settings=settings)


@app.route("/delete/<clock_number>", methods=["GET", "POST"])
def delete_employee(clock_number):
    settings = list(mongo.db.index_template.find())
    employess = mongo.db.employess.find_one({"clock_nr": int(clock_number)})
    # Check if autentificated
    if 'user' not in session:
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            clock_nr_v = request.form.get("clock-number-v")
            if clock_number == clock_nr_v:
                mongo.db.employess.delete_one({"clock_nr": int(clock_nr_v)})
                flash("Employee was successfully deleted!")
                return redirect(url_for("employess"))

            flash("Confirmation Clock in Number is Wrong, Please try Again!")
            return render_template("edit-employee.html", employess=employess, settings=settings)


@app.route("/settings/", methods=["GET", "POST"])
def settings():
    settings = list(mongo.db.index_template.find())
    if request.method == "POST":
        brand_name = request.form.get("brand-name")
        navbar_color = request.form.get("navbar-color")
        menu_text_color = request.form.get("menu-text-color")
        for set in settings:
            if brand_name:
                mongo.db.index_template.update_one({"brand_text": set["brand_text"]}, {
                    "$set": {"brand_text": request.form.get("brand-name")}})
            elif navbar_color:
                mongo.db.index_template.update_one({"navbar_color": set["navbar_color"]}, {
                    "$set": {"navbar_color": request.form.get("navbar-color")}})
            elif menu_text_color:
                mongo.db.index_template.update_one({"navbar_text_color": set["navbar_text_color"]}, {
                    "$set": {"navbar_text_color": request.form.get("menu-text-color")}})

        print(settings)
        return redirect(url_for("settings", settings=settings))
    print(settings)
    return render_template("settings.html", settings=settings)


@ app.route("/logout")
def logout():
    if 'user' not in session:
        # Preventing error page if direct link acces. Redirecting to login.
        flash("You need to be authenticated to access this page!")
        return redirect(url_for("login"))

    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
