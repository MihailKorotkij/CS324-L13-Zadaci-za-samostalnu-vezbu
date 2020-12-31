from flask import Flask
from strana1 import prva_strana
from strana2 import druga_strana
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/strana1')
def strana1():
    content = prva_strana()
    return content

@app.route('/strana2')
def strana2():
    content = druga_strana()
    return content