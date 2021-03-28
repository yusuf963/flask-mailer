from flask import Flask, request
import smtplib

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


@app.route("/registeration")
def register():
    name = "John"
    email = "yusufm.musa963@gmail.com"
    # if not name or not email:
    #     return 'inter either name or email address'
    message = f"Dear {name}, You are successfully reegistered "

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("mohammad963yusuf@gmail.com", "1991mohammadyusuf")
    server.sendmail("mohammad963yusuf@gmail.com", email, message)
    return "welcome111"
