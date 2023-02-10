#!/bin/bash

# refer to https://flask.palletsprojects.com/en/2.0.x/server/
# notice which python venv (or what path) you are in!

FLASK_APP=api_service FLASK_ENV=development flask run
# Use default host, and default port 5000
# flask run [OPTIONS]
# -h, --host TEXT                 The interface to bind to.
# -p, --port INTEGER              The port to bind to.