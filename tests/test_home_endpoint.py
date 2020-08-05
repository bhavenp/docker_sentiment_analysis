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
	response = client.post('/', data=data)
	assert response.status_code == 200

	# Check that right HTML page is being generated
	assert b"Your sentence:" in response.data


