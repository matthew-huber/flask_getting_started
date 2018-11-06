from flask import Flask, jsonify, request
from math import sqrt
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


@app.route("/distance", methods=["POST"])
def distance():
    dict_r = request.get_json()
    print(dict_r["a"])
    print(dict_r["b"])
    xdiff_squared = (dict_r["a"][0]-dict_r["b"][0])**2
    ydiff_squared = (dict_r["a"][1]-dict_r["b"][1])**2
    distance = sqrt(xdiff_squared + ydiff_squared)
    
    json_return = {
            "distance": distance,
            "a": dict_r["a"],
            "b": dict_r["b"]
            }
    
    return jsonify(json_return) 

if __name__ == "__main__":
    app.run(host="127.0.0.1")

