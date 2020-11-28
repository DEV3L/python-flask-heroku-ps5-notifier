import os

import pymongo
from pymongo.database import Database

from src.services.logging_service import LoggingService

logger = LoggingService('mongo_db')


class MongoDb:
    db = None

    @classmethod
    def instance(cls, *, force: bool = False, mongodb_uri: str = None) -> Database:
        if force or not cls.db:
            logger.info('Connecting to MongoDb')
            mongodb_uri = mongodb_uri or os.getenv('MONGODB_URI')
            client = pymongo.MongoClient(mongodb_uri)
            cls.db = client['ps5_notifier']

        return cls.db
