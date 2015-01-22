from flask import Flask
app = Flask(__name__)

## Rollbar init code. You'll need the following to use Rollbar with Flask.
## This requires the 'blinker' package to be installed

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception


@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token for the demo app: https://rollbar.com/demo
        'fc316ac1f7404dc28af26d5baed1416c',
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
    print "in hello"
    x = None
    x[5]
    return "Hello World!"


if __name__ == '__main__':
    app.run()
