# test that hello endpoint is working
def test_hello(client):
	response = client.get('/hello')
	assert response.data == b'Hello World!'

# test that home endpoint is working
def test_index(client):
	response = client.get('/')
	assert response.status_code == 200 
