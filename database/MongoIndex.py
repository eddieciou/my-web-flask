from database.MongoConn import MongoConn
from pymongo import IndexModel, DESCENDING


class MongoIndex:

    def __init__(self):
        self.db = MongoConn().conn()['backend']

    def create_backend_index(self):
        self.__users_index()
        self.__role_index()
        self.__permission_index()

    def __users_index(self):
        index_account = IndexModel([("account", DESCENDING)], unique=True)
        index_mail = IndexModel([("mail", DESCENDING)], unique=True)
        self.db['users'].create_indexes([index_account, index_mail])

    def __role_index(self):
        index_role = IndexModel([("role_name", DESCENDING), ("agent_id", DESCENDING)], unique=True)
        self.db['role'].create_indexes([index_role])

    def __permission_index(self):
        pass
