from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def hello_world(name:str=""):
    #return "<p>Hello, World!</p>"
    #return "<h1>Hello, 您好歡迎進入!</h1>"
    return f"<h1>Hello,{name}您好!</h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'