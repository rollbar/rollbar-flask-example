# rollbar-flask-example

A simple example [Flask](http://flask.pocoo.org/) app, showing how to use [Rollbar](https://rollbar.com) (the error tracking service) with Flask.

## How to run

This example requires Python 3 (or 2.6+), pip, and virtualenv.

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python hello.py
```

That will start the server on [localhost:5000](http://localhost:5000) .

Or run with gunicorn:

```
gunicorn hello:app
```

which will start the server on [localhost:8000](http://localhost:8000) .

## Note on requirements

We tested with the listed versions in requirements.txt, but other versions of flask, blinker, and gunicorn are likely to work as well. Note that `blinker` is required. `gunicorn` is only required to run via gunicorn.


