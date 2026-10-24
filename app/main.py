from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Multi-Stage CI/CD Pipeline",
        "message": "Application is running",
        "status": "success"
    }), 200

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/pipeline")
def pipeline():
    return jsonify({
        "pipeline": "Multi-Stage CI/CD",
        "stages": [
            "Build",
            "Test",
            "Package",
            "Deploy",
            "Verify"
        ],
        "status": "ready"
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)