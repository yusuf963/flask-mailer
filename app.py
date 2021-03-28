from flask import Flask, request
import smtplib

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


@app.route("/registeration")
def register():
    name = "John"
    email = "reciptes@gmail.com"
    # if not name or not email:
    #     return 'inter either name or email address'
    message = f"Dear {name}, You are successfully reegistered "

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your sender email here", )
    server.sendmail("your sender email here", email, message)
    return "welcome"
