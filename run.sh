#!/bin/bash

# 'app.run_app' is the module name, and 'create_app()' is the callable that should be found
# in the module. We need quotes around the <module>:<callable> because the callable returns
# the actual application as defined by our application factory pattern.

# '-w 2' runs the Flask application with 2 worker processes.
exec gunicorn -w 2 --bind 0.0.0.0:8000 "app.run_app:create_app()"