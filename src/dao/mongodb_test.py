import os
from unittest.mock import patch

from src.dao.mongodb import MongoDb


@patch('src.dao.mongodb.logger')
@patch('src.dao.mongodb.pymongo')
def test_mongodb_instance_only_ever_called_once(mock_pymongo, mock_logger):
    expected_mongodb_uri = 'mongodb_uri'
    os.environ['MONGODB_URI'] = expected_mongodb_uri

    MongoDb.db = None

    result_db = MongoDb.instance()
    MongoDb.instance()

    mock_pymongo.MongoClient.assert_called_with(expected_mongodb_uri)
    assert 1 == mock_pymongo.MongoClient.call_count
    assert mock_pymongo.MongoClient.return_value['ps5_notifier'] == result_db
    assert mock_logger.info.called
