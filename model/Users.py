from database.MongoConn import MongoConn


class Users:
    def __init__(self):
        self.db = MongoConn().conn()['backend']

    def authenticate(self, account: str, password_hash: str):
        return self.db['users'].find_one({"account": account, "password": password_hash})
