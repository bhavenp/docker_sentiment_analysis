def test_predict1(client):
	data = {"sentences": ["This place is the best!"]}
	response = client.post('/predict', json=data)
	assert response.status_code == 200 # Check for successful status code

	# Check that 'pred' array has correct size
	json_data = response.get_json()
	assert len(json_data['pred']) == 1

def test_predict2(client):
	data = {"sentences": ["This place is the worst!", "This place is the best!", "I love this place."]}
	response = client.post('/predict', json=data)
	assert response.status_code == 200 # Check for successful status code

	# Check that 'pred' array has correct size
	json_data = response.get_json()
	assert len(json_data['pred']) == 3


def test_predict_with_get(client):
	response = client.get('/predict')
	json_data = response.get_json()
	assert json_data['msg'] # Check that a String is sent back in the response
