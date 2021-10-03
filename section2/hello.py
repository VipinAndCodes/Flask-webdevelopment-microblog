from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h> hiiii </h> '

@app.route('/<name>')
def user(name):
    return '<h> hii {} </h>'.format(name)