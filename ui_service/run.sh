#!/bin/bash


if [ $# -eq 0 ]
then
	# 'run_app' is the module name, and 'create_app()' is the callable that should be found
	# in the module. We need quotes around the <module>:<callable> because the callable returns
	# the actual application as defined by our application factory pattern.

	# '-w 2' runs the Flask application with 2 worker processes.

	exec gunicorn -w 1 --bind 0.0.0.0:8001 "run_app:create_app()"

else # An extra argument was provided, which must be the URL for the ml-service
	exec gunicorn -w 1 --bind 0.0.0.0:8001 "run_app:create_app(\"$1\")"
fi
