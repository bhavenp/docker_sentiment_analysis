'''
This file contains fixtures, which are setup functions that each test 
function in the other files will use. These fixtures for the 'app' and
'client' allow each test to receive the same setup, creating 
consistency.
'''
import pytest

import run_app


@pytest.fixture
def app():
	app = run_app.create_app()
	return app

@pytest.fixture
def client(app):
	'''
	Tests will use the 'client' object return by the 'app' to make 
	requests to the application without running the server.
	'''
	return app.test_client()