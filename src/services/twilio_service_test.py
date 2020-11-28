from unittest.mock import patch

from src.services.twilio_service import TwilioService, ACCOUNT_SID, AUTH_TOKEN, TWILIO_TO, TWILIO_FROM


@patch('src.services.twilio_service.Client')
def test_twilio_service_instance_initializes_client_with_environment_variables(mock_client):
    twilio_service = TwilioService()

    mock_client.assert_called_with(ACCOUNT_SID, AUTH_TOKEN)

    assert twilio_service.client == mock_client.return_value


@patch('src.services.twilio_service.Client')
def test_send_message_sends_to_number_from_number_with_message(mock_client):
    expected_message = "Hello, world!"

    twilio_service = TwilioService()
    twilio_service.send_message(expected_message)

    mock_client.return_value.api.account.messages.create.assert_called_with(
        to=TWILIO_TO,
        from_=TWILIO_FROM,
        body=expected_message)
