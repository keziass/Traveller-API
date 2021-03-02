from nameko.rpc import rpc
import schemas

from dependencies import db_dependencies
from dependencies import redis_dependencies

import uuid

class UserService:
    name = 'user_service'

    database = db_dependencies.Database()
    redis = redis_dependencies.Redis()

    def __init__(self):
        print("Service Constructor")

    @rpc
    def login(self, email, password):
        res = self.database.log_in(email, password)
        if res['err'] == 0:
            session_id = str(uuid.uuid1())
            res['session_id'] = session_id
            self.redis.set_data(session_id, res['data'])
        self.database.close_connection()
        return schemas.LoginResultSchema().dump(res)

    @rpc
    def check_login(self, session_id):
        res = self.redis.is_logged_in(session_id)
        data = {}
        if res:
            data = self.redis.get_data(session_id)
        return {'status': res, 'data': data}

    @rpc
    def get_all_user(self):
        user = self.database.get_all_active_user()
        self.database.close_connection()
        return schemas.UserSchema(many=True).dump(user)

    @rpc
    def get_user_by_id(self, id):
        user = self.database.get_user_by_id(id)
        self.database.close_connection()
        return schemas.UserSchema().dump(user)
    
    @rpc
    def check_active_user(self, id):
        user = self.database.get_user_by_id(id)
        self.database.close_connection()
        return user['status'] == 'ACTIVE'

    @rpc
    def check_user(self, id):
        user = self.database.get_user_by_id(id)
        self.database.close_connection()
        if user is None:
            return False
        else:
            return True

    @rpc
    def search_user(self, name):
        user = self.database.search_user(name)
        self.database.close_connection()
        return schemas.UserSchema(many=True).dump(user)

    @rpc
    def create_user(self, data):
        resultMsg = {
            'code': 200,
            'msg': 'Success to add User'
        }
        self.database.create_user(data)
        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)


    @rpc
    def edit_user(self, id, data):
        resultMsg = {
            'code': 0,
            'msg': ''
        }
        print(self.check_user(id))
        if self.check_user(id):
            resultMsg['code'] = 200
            resultMsg['msg'] = 'Success update data'
            self.database.edit_user(id, data)
        else:
            resultMsg['code'] = 404
            resultMsg['msg'] = 'Data user not found'

        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)

    def __del__(self):
        print("Service Destructor")

    
    @rpc
    def delete_user(self, id):
        resultMsg = {
            'code': 0,
            'msg': ''
        }
        print(self.check_user(id))
        if self.check_user(id):
            resultMsg['code'] = 200
            resultMsg['msg'] = 'Success delete User'
            self.database.delete_user(id)
        else:
            resultMsg['code'] = 404
            resultMsg['msg'] = 'Data User not found'

        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)