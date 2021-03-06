from flask import request
from flask import jsonify
from flask import Flask
import pybase64

app = Flask(__name__)

@app.route("/j", methods=["GET"])
def getJSON():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return jsonify({'ip': ip}), 200

@app.route("/", methods=["GET"])
def getIP():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return str(ip) + str('\n'), 200


@app.route("/bd/<section>")
def base64Decode(section):
    assert section == request.view_args['section']
    try:
        return str(pybase64.standard_b64decode(str(section)).decode('utf-8'))  + str('\n'), 200
    except:
        return "Please check your parameter. QAQ"

@app.route("/b/<section>")
def base64Encode(section):
    assert section == request.view_args['section']
    try:
        return str(pybase64.standard_b64encode(str(section).encode('UTF-8')).decode('utf-8'))  + str('\n'), 200
    except:
        return "Please check your parameter. QAQ"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
