import os

# App configuration
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "Your Secret Key")
os.environ.setdefault(
    "MONGO_URI", "your mongo URI")
os.environ.setdefault("MONGO_DBNAME", "DB Name")

# Email configuration
os.environ.setdefault("MAIL_SERVER", "0.0.0.0")
os.environ.setdefault("MAIL_PORT'", "2525")
os.environ.setdefault("MAIL_USERNAME'", "Mail Username")
os.environ.setdefault("MAIL_PASSWORD'", "Password")
os.environ.setdefault("MAIL_USE_TLS'", "True")
os.environ.setdefault("MAIL_USE_SSL'", "False")
os.environ.setdefault("MAIL_DEFAULT_SENDER'", "Your email address")
