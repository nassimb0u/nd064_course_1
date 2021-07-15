from flask import Flask
from flask import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def health_check():
    response = app.response_class(
        response=json.dumps({"result": "OK - healty"}),
        status=200,
        mimetype="application/json"
    )
    return response

@app.route("/metrics")
def get_metrics():
    return {
        "status": "success",
        "code": 0,
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
