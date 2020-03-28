import logging
import jwt

from flask import g
from time import time
from utils.AESCipherUtil import AESCipherUtil

log = logging.getLogger('Auth')


TOKEN_EXPIRATION = 86400
SECRET_KEY = "5d0c2f33c9e82e3c723dcab2"
AES_KEY = "abf5b03e755f6ae4d0f14b8be4b87691"

cipher = AESCipherUtil(AES_KEY)


class AuthToken:
    @staticmethod
    def verify_token(encrypted_token):
        token = None
        try:
            token = cipher.decrypt(encrypted_token)
            obj = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = obj["sub"]
            log.info(f'Operation executed by:{user_id}')
            if user_id:
                g.current_user_id = user_id
            return True
        except (jwt.DecodeError, TypeError, ValueError) as e:
            log.warning(f'Invalid token:{e}')
            return False
        except jwt.ExpiredSignatureError:
            user_payload = jwt.decode(token, SECRET_KEY, options={'verify_exp': False})
            user_id = user_payload["sub"]
            logging.info(f"Expired token of {user_id}")
            return False

    @staticmethod
    def generate_token(payload=None):
        if payload is None:
            payload = {}
        payload.update({
            'exp': time() + TOKEN_EXPIRATION
        })
        jwt_token = jwt.encode(payload, SECRET_KEY)
        token = cipher.encrypt(jwt_token)
        return token
