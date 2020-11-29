import os

from dotenv import load_dotenv

load_dotenv()

from twilio.rest import Client

if __name__ == '__main__':
    # Find these values at https://twilio.com/user/account
    # To set up environmental variables, see http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    twilio_to = os.environ['TWILIO_TO']
    twilio_from = os.environ['TWILIO_FROM']

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=twilio_to,
        from_=twilio_from,
        body="Hello, world!")
