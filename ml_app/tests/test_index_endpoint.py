'''
This file holds tests to ensure the '/index' endpoint works as 
expected. The '/home' endpoint can be hit with GET or POST Requests.
For POST Requests, the data comes in as a dictionary with a key 
called 'sentence' mapping to a String that user wants the sentiment for.
'''

# test that index endpoint is working
def test_hello(client):
	response = client.get('/')

	assert response.status_code == 200
	assert response.data == b'ML model application is running!'