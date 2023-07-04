from __future__ import print_function

from flask import Flask
app = Flask(__name__)

## Rollbar init code. You'll need the following to use Rollbar with Flask.
## This requires the 'blinker' package to be installed

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception

## XXX hack to make request data work with pyrollbar <= 0.16.3
def _get_flask_request():
    print("Getting flask request")
    from flask import request
    print("request:", request)
    return request
rollbar._get_flask_request = _get_flask_request

def _build_request_data(request):
    return rollbar._build_werkzeug_request_data(request)
rollbar._build_request_data = _build_request_data
## XXX end hack


with app.app_context():
    rollbar.init(
        # use a post_server_item access token for your Rollbar project
        'ACCESS_TOKEN',
        # environment name
        'flasktest',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


## To set up Person Tracking, implement a custom request_class that has a `rollbar_person` property.
## If you already have a custom request class, just add the rollbar_person property method to it.

from flask import Request
class CustomRequest(Request):
    @property
    def rollbar_person(self):
        # 'id' is required, 'username' and 'email' are indexed but optional.
        # all values are strings.
        return {'id': '123', 'username': 'test', 'email': 'test@example.com'}

app.request_class = CustomRequest


## Simple flask app below

@app.route('/')
def hello():
    print("in hello")
    x = None
    x[5]
    return "Hello World!"


if __name__ == '__main__':
    app.run()
