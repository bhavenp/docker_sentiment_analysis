import pytest

from app import run_app


@pytest.fixture
def app():
	app = run_app.create_app()
	yield app

@pytest.fixture
def client(app):
	'''Tests will use the client to make requests to the application without running the server.'''
	return app.test_client()