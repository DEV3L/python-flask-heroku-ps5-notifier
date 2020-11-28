import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.services.twilio_service import TwilioService

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_to = os.environ['TWILIO_TO']
twilio_from = os.environ['TWILIO_FROM']


@patch('src.services.twilio_service.Client')
def test_twilio_service_instance_initializes_client_with_environment_variables(mock_client):
    twilio_service = TwilioService()

    mock_client.assert_called_with(account_sid, auth_token)

    assert twilio_service.client == mock_client.return_value


@patch('src.services.twilio_service.Client')
def test_send_message_sends_to_number_from_number_with_message(mock_client):
    expected_message = "Hello, world!"

    twilio_service = TwilioService()
    twilio_service.send_message(expected_message)

    mock_client.return_value.api.account.messages.create.assert_called_with(
        to=twilio_to,
        from_=twilio_from,
        body=expected_message)
