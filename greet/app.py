from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return(add(3,5))

@app.route('/welcome/home')
def say_welcome_home():
    return("welcome home")

@app.route('/welcome/back')
def say_welcome_back():
    return("welcome back")