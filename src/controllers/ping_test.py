def test_ping_returns_200(flask_test_client):
    response = flask_test_client.get('/ping')
    assert 200 == response.status_code


def test_pingz_returns_404(flask_test_client):
    response = flask_test_client.get('/pingz')
    assert 404 == response.status_code


def test_raise_returns_500(flask_test_client):
    response = flask_test_client.get('/raise')
    assert 500 == response.status_code
