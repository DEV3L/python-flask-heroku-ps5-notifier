from unittest.mock import patch

from src.services.twilio_service import ACCOUNT_SID, AUTH_TOKEN, TWILIO_TO, TWILIO_FROM


@patch('src.services.twilio_service.Client')
def test_twilio_returns_200(mock_client, flask_test_client):
    expected_message = "Hello, world!"

    response = flask_test_client.get('/twilio')

    mock_client.assert_called_with(ACCOUNT_SID, AUTH_TOKEN)
    mock_client.return_value.api.account.messages.create.assert_called_with(
        to=TWILIO_TO,
        from_=TWILIO_FROM,
        body=expected_message)

    assert 200 == response.status_code
