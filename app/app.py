from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>AWS Cloud Infrastructure Project</h1>
    <p>Flask application is running successfully.</p>
    <p>Infrastructure: AWS EC2 + Docker + Linux</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-app"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
