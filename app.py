from flask import request
from flask import jsonify

@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
