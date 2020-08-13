'''
This file holds tests to ensure the '/home' endpoint works as 
expected. The '/home' endpoint can be hit with GET or POST Requests.
For POST Requests, the data comes in as a dictionary with a key 
called 'sentence' mapping to a String that user wants the sentiment for.
'''

# test that hello endpoint is working
def test_hello(client):
	response = client.get('/hello')
	assert response.data == b'Hello World!'

# test that home endpoint is working
def test_index(client):
	response = client.get('/')
	assert response.status_code == 200

# test that we can make a prediction using the homepage
def test_predict_at_index(client):
	data = {"sentence": "This place is the best!"}
	response = client.post('/', data=data, follow_redirects=True)
	assert response.status_code == 200

	# Check that right HTML page is being generated
	assert b"Your sentence:" in response.data

	# Check that another prediction can be made on this page
	data = {"sentence": "This place is the worst!"}
	response = client.post('/', data=data, follow_redirects=True)
	assert response.status_code == 200

	# Check that right HTML page is being generated
	assert b"Your sentence:" in response.data



