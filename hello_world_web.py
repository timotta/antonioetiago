from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<body style='padding:0; margin:0'><div style='background: black'><h1 style='color: white'>Hello, World!</h1> </div></body>"