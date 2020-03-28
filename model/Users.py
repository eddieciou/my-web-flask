import logging
import bson
from database.MongoConn import MongoConn


class Users:
    def __init__(self):
        self.logging = logging.getLogger(__name__)
        self.logging.info('User __init__')

        self.db = MongoConn().conn()['backend']

    def authenticate(self, account: str, password_hash: str):
        self.logging.info('authenticate')
        return self.db['users'].find_one({"account": account, "password": password_hash})

    def get_user_info(self, user_id: str):
        self.logging.info('get_user_info')

        object_id = bson.objectid.ObjectId(user_id)

        return self.db['users'].find_one({"_id": object_id})
