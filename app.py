from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask deployed on the Cloud!"

@app.route("/api/info")
def info():
    return jsonify({
        "course": "Cloud Computing",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(debug=True)