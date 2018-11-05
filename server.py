from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    name = {
            "name": "Matthew"
            }
    return jsonify(name)

if __name__ == "__main__":
    app.run(host="127.0.0.1")

