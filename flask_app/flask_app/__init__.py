from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def get_api():
    return jsonify({"message": "Hello from Flask API!"})

@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.json
    return jsonify({"received": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
