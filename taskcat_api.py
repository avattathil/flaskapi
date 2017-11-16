#!/usr/bin/env python
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5/day", "50/day"]
)

@app.route('/')
def index():
    return {'taskcat': 'running'}


@app.route('/status/')
@limiter.limit("5/day")
def status():
    return 'status'

@app.route('/api/')
def api():
    return  "01"

@app.route('/ping')
@limiter.exempt
def ping():
    return "PONG"

if __name__ == "__main__":
    app.run(debug=True)