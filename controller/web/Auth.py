# import logging
from flask import request
from models.Users import Users
from commons.Response import response
from commons.AuthToken import AuthToken


class Auth:
    def __init__(self):
        pass
        # self.logging = logging.getLogger(__name__)

    def login(self):
        # self.logging.info("login")

        data = request.json
        account = data.get('account')
        password = data.get('password')
        user = Users.query.filter_by(username=account).first()

        # 驗證成功
        if user is not None and user.verify_password(password):
            jwt_token = AuthToken.generate_token({
                'sub': user.id
            })

            data = {
                "account": account,
                "user_id": user.id,
                "user_name": user.username,
                "role_id": str(user.role_id),
                # TODO 以role_id 查role name
                "role_name": "角色名稱",
                # TODO user entry point
                "entry_point": "user entry point"
            }
            return response(0, "", data, headers={"Authorization": jwt_token})

        # 驗證失敗
        return response(999, "Login Fail")

