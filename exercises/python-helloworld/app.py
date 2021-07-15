from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('"/" endpoint was reached')
    return "Hello World!"

@app.route("/status")
def health_check():
    app.logger.info('"/status" endpoint was reached')
    response = app.response_class(
        response=json.dumps({"result": "OK - healty"}),
        status=200,
        mimetype="application/json"
    )
    return response

@app.route("/metrics")
def get_metrics():
    app.logger.info('"/metrics" endpoint was reached')
    return {
        "status": "success",
        "code": 0,
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }

if __name__ == "__main__":
    logging.basicConfig(
        filename="app.log",
        format="{levelname}:{name}: [{asctime}] {message}",
        datefmt="%a %d %b %Y %X",
        style="{",
        level=logging.DEBUG
    )
    app.run(host='0.0.0.0')
