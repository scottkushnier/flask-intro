# Put your app in here.

from flask import Flask, request

from operations import add, sub, mult, div


app = Flask(__name__)

@app.route('/add', methods=['GET'])
def do_add():
    return(str(add(int(request.args['a']), int(request.args['b']))))

@app.route('/sub', methods=['GET'])
def do_sub():
    return(str(sub(int(request.args['a']), int(request.args['b']))))

@app.route('/mult', methods=['GET'])
def do_mult():
    return(str(mult(int(request.args['a']), int(request.args['b']))))

@app.route('/div', methods=['GET'])
def do_div():
    return(str(div(int(request.args['a']), int(request.args['b']))))

@app.route('/welcome')
def do_welcome():
    return("hi")