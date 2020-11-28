def test_swagger_returns_200(flask_test_client):
    response = flask_test_client.get('/swagger')
    assert 308 == response.status_code


def test_swagger_spec_returns_200(flask_test_client):
    response = flask_test_client.get('/swagger_spec')
    assert 200 == response.status_code
    assert response.json
