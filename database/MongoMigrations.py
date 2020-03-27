from database.MongoConn import MongoConn
from utils.DateTimeUtil import DateTimeUtil
from database.MongoIndex import MongoIndex


class MongoMigrations:
    def __init__(self):
        self.db = MongoConn().conn()

    def init(self):
        object_id = self.__role().__str__()
        self.__users(object_id)
        self.__permission(object_id)

    def __users(self, object_id):
        data = {
            "_id": object_id,
            "name": "root",
            "agent_id": "root",
            "role_id": object_id,
            "account": "root",
            "password": "9878a67e7544cb52784aa60c47f706f4bdcaef3ea3fb0b6e0560f71e2f0e8aff",  # %TGB6yhn 的hash值
            "mail": "root@gmail.com",
            "entry_point": "main",
            "created_at": DateTimeUtil.get_now_dtm_obj(),
            "updated_at": DateTimeUtil.get_now_dtm_obj(),
            "remember_token": False
        }
        self.db["backend"]["users"].insert(data)

    def __role(self):
        data = {
            "role_name": "root",
            "agent_id": "root"
        }
        return self.db["backend"]["role"].insert(data)

    def __permission(self, object_id):
        fun_data = [
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "BSS",
                "func_group_id": "_",
                "name": "儀表板",
                "func_sort": 1,
                "func_url": "/dashboard",
                "level": 1,
                "icon": [
                    "fas",
                    "tachometer-alt"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAA",
                "func_group_id": "_",
                "name": "總代理管理",
                "func_sort": 2,
                "func_url": None,
                "level": 1,
                "icon": [
                    "fas",
                    "cogs"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAA004",
                "func_group_id": "SAA",
                "name": "遊戲商管理",
                "func_sort": 1,
                "func_url": "/sites",
                "level": 2,
                "icon": [
                    "far",
                    "window-restore"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAA001",
                "func_group_id": "SAA",
                "name": "使用者管理",
                "func_sort": 2,
                "func_url": "/user",
                "level": 2,
                "icon": [
                    "fas",
                    "users-cog"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAA002",
                "func_group_id": "SAA",
                "name": "角色管理",
                "func_sort": 3,
                "func_url": "/permission",
                "level": 2,
                "icon": [
                    "fas",
                    "user-tie"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAB",
                "func_group_id": "_",
                "name": "子代理管理",
                "func_sort": 3,
                "func_url": None,
                "level": 1,
                "icon": [
                    "fas",
                    "users"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAB001",
                "func_group_id": "SAB",
                "name": "創建子代理",
                "func_sort": 1,
                "func_url": "/member/info",
                "level": 2,
                "icon": [
                    ""
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAB002",
                "func_group_id": "SAB",
                "name": "子代理遊戲商管理",
                "func_sort": 2,
                "func_url": "/member/event",
                "level": 2,
                "icon": [
                    "fas",
                    "clipboard-list"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAB003",
                "func_group_id": "SAB",
                "name": "子代理金流上限管理",
                "func_sort": 3,
                "func_url": "/member/member_grade",
                "level": 2,
                "icon": [
                    ""
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAH",
                "func_group_id": "_",
                "name": "報表管理",
                "func_sort": 10,
                "func_url": None,
                "level": 1,
                "icon": [
                    "fas",
                    "chart-bar"
                ]
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "funcList",
                "func_id": "SAH001",
                "func_group_id": "SAH",
                "name": "報表管理",
                "func_sort": 1,
                "func_url": "/report/operation",
                "level": 2,
                "icon": [
                    ""
                ]
            }
        ]

        btn_data = [
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BSS001001",
                "func_group_id": "BSS",
                "name": "檢視",
                "func_sort": 1
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA001001",
                "func_group_id": "SAA001",
                "name": "查詢檢視",
                "func_sort": 1
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA001002",
                "func_group_id": "SAA001",
                "name": "新增使用者",
                "func_sort": 2
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA001003",
                "func_group_id": "SAA001",
                "name": "停用啟用",
                "func_sort": 3
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA001004",
                "func_group_id": "SAA001",
                "name": "修改",
                "func_sort": 4
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA002001",
                "func_group_id": "SAA002",
                "name": "查詢檢視",
                "func_sort": 1
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA002002",
                "func_group_id": "SAA002",
                "name": "新增角色",
                "func_sort": 2
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA002003",
                "func_group_id": "SAA002",
                "name": "修改",
                "func_sort": 3
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA002004",
                "func_group_id": "SAA002",
                "name": "刪除",
                "func_sort": 4
            },
            {
                "role_id": object_id,
                "agent_id": "root",
                "role_category": "btnList",
                "func_id": "BAA004001",
                "func_group_id": "SAA004",
                "name": "查詢檢視",
                "func_sort": 1
            }
        ]
        self.db["backend"]["permission"].insert_many(fun_data)
        self.db["backend"]["permission"].insert_many(btn_data)
        return True


if __name__ == "__main__":
    MongoIndex().create_backend_index()
    MongoMigrations().init()
