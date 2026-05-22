from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Docker Hub + Azure ACR Multi Registry CI/CD</h1>
    <p>Task 4 Deployment Success!</p>
    <p>Student: jihyun2144</p>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
