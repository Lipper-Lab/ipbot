from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
