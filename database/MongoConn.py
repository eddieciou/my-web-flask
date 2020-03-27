import logging
from pymongo import MongoClient
from config import MongoDB


class MongoConn:
    log = logging.getLogger('MongoConn')
    connection = None

    def __connect_db(self):
        self.log.info('connect to Mongo DB')
        return MongoClient(
            f"mongodb://{MongoDB.mongo_username}:{MongoDB.mongo_password}@{MongoDB.mongo_host}:{MongoDB.mongo_port}/"
            f"{MongoDB.mongo_auth_db}", tz_aware=False, connect=False,
            serverselectiontimeoutms=MongoDB.mongo_timeout_sec, ssl=MongoDB.mongo_ssl
        )

    def conn(self):
        if self.connection is None:
            self.connection = self.__connect_db()
        return self.connection
