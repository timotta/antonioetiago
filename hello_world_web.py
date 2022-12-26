from flask import Flask, request

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


@app.route("/sleep")
def sleep_endpoint():
    from time import sleep
    sleep(1)
    return """ok"""


@app.post("/command/unlock")
def command_unlock():
    print(request.args["secret"])
    print(request.method)
    print(request.json)

    if request.json["parameters"][0] == 412:
        return {"error": "INVALID_STATE"}, 412

    if request.json["parameters"][0] < 600:
        return "erro", request.json["parameters"][0]

    return {}, 200


@app.route("/backbone/payload/<ad_id>/<action_id>")
def backbone_payload(ad_id, action_id):
    if action_id == "500":
        return "Flask error", 500
    if action_id == "503":
        return "Flask error", 503
    if action_id == "404":
        return "Flask 404", 404
    if action_id == "403":
        return {
            "action": None,
            "ad": {
                "ad_id": ad_id,
                "list_id": ad_id,
                "type": "sell",
                "status": "deleted",
                "category": 7020,
            }
        }, 200
    if action_id == "402":
        return {}, 200
    return {
        "action": {
            "queue": "normal",
            "action_id": action_id,
            "action_type": "gallery",
        },
        "ad": {
            "ad_id": ad_id,
            "list_id": ad_id,
            "type": "sell",
            "status": "deleted",
            "category": 7020,
        }
    }, 200


@app.route("/ventricle/entities")
def ventricle_entities():
    if len(request.args.get('list_id')) == 3:
        return "Flask simulated errors", int(request.args.get('list_id'))

    return {
        "entity_instance_version": {
            "extra_instance_ids": {
                "ad_id": 123
            },
            "data": {
                "category": 7070
            }
        }
    }, 200
