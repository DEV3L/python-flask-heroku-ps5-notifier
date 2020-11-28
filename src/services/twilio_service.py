import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class TwilioService:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']

        self.twilio_to = os.environ['TWILIO_TO']
        self.twilio_from = os.environ['TWILIO_FROM']

        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, message: str):
        self.client.api.account.messages.create(
            to=self.twilio_to,
            from_=self.twilio_from,
            body=message)
