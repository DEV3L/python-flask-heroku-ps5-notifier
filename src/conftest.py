import base64
import os
from typing import Dict
from unittest.mock import MagicMock

import pytest
from flask.testing import FlaskClient
from pymongo.database import Database

from app import app as flask_app
from src.dao.mongodb import MongoDb


@pytest.fixture
def flask_test_client() -> FlaskClient:
    # suppress error logging
    import app
    app.logger = MagicMock()

    flask_test_client = flask_app.test_client()
    flask_test_client.testing = True

    return flask_test_client


@pytest.fixture
def authorized_header_with_json_content_type() -> Dict:
    basic_auth_username = os.getenv('BASIC_AUTH_USERNAME')
    basic_auth_password = os.getenv('BASIC_AUTH_PASSWORD')
    authorization = f'{basic_auth_username}:{basic_auth_password}'

    encoded_authorization_bytes = base64.b64encode(authorization.encode('utf-8'))
    encoded_authorization_str = str(encoded_authorization_bytes, 'utf-8')

    headers = {'Content-Type': 'application/json',
               'Authorization': f'Basic {encoded_authorization_str}'}
    return headers


@pytest.fixture
def mongo_db() -> Database:
    _mongo_db = MongoDb.instance(force=True, mongodb_uri='mongodb://localhost:27017/')
    return _mongo_db
