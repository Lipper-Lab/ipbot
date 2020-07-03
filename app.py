from flask import request
from flask import jsonify
from flask import Flask

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
    return str(ip), 200
    
    

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
