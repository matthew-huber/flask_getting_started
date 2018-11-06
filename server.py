from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    name = {
            "name": "Matthew"
            }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    message = {
            "message": "Hello there, {}".format(name)
            }
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="127.0.0.1")

