import os

from flask_httpauth import HTTPBasicAuth

auth_service = HTTPBasicAuth()

BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')


@auth_service.verify_password
def verify_password(username, password):
    return BASIC_AUTH_USERNAME == username and BASIC_AUTH_PASSWORD == password
