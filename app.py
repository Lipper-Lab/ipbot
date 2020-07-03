from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return jsonify({'ip': ip}), 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
