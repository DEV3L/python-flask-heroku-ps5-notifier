import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', 'TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', 'TWILIO_AUTH_TOKEN')
TWILIO_TO = os.environ.get('TWILIO_TO', 'TWILIO_TO')
TWILIO_FROM = os.environ.get('TWILIO_FROM', 'TWILIO_FROM')


class TwilioService:
    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN

        self.twilio_to = TWILIO_TO
        self.twilio_from = TWILIO_FROM

        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, message: str):
        self.client.api.account.messages.create(
            to=self.twilio_to,
            from_=self.twilio_from,
            body=message)
