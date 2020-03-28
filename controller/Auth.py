import hmac
import hashlib
import logging
from flask import request
from config import setting
from controller.Response import response
from model.Users import Users
from commons.AuthToken import AuthToken


class Auth:
    def __init__(self):
        self.logging = logging.getLogger(__name__)

    def login(self):
        self.logging.info('login')

        data = request.json
        account = data.get('account')
        password = data.get('password')
        user = self.__authenticate(account, password)

        if user is None:
            return response(999, "Login Fail")

        user_id = user['_id'].__str__()
        jwt_token = AuthToken.generate_token({
            'sub': user_id
        })

        data = {
            "account": account,
            "usr_id": user['_id'],
            "usr_name": user['name'],
            "role_id": user['role_id'],
            "role_name": "系統管理者",
            "entry_point": user['entry_point']
        }
        return response(0, "", data, Authorization=jwt_token)

    def __authenticate(self, account: str, password: str):
        self.logging.info('__authenticate')
        password_hash = self.__password_hash(password)
        user = Users().authenticate(account, password_hash)
        return user

    def __password_hash(self, password: str):
        self.logging.info('__password_hash')
        password_hash = hmac.new(setting.app_key.encode('utf-8'), password.encode('utf-8'), hashlib.sha256)
        return password_hash.hexdigest()

    def hello(self):
        return {
            'hello': 'hello'
        }
