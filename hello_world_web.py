from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <body style='padding:0; margin:0; text-align: center'>
            <div style='background: black'>
                <h1 style='color: white'>Testes de Antonio e Tiago na Web</h1>
            </div>
            <img src="/static/IMG_20220903_124138.jpg" width=800 />
        </body>
    """