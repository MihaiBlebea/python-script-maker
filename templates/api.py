from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	return jsonify({"status": "OK"})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ.get("HTTP_PORT", 5000)))