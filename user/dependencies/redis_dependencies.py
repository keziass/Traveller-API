from nameko.extensions import DependencyProvider

import redis
import pickle


class RedisWrapper:
    connection = None

    def __init__(self, connection):
        print("Redis Wrapper Constructor")
        self.connection = connection

    def set_data(self, key, value, expire=90 * 30):
        value_byte = pickle.dumps(value)
        self.connection.set(key, value_byte, ex=expire)

    def get_data(self, key):
        value_byte = self.connection.get(key)
        value = pickle.loads(value_byte)
        return value

    def is_logged_in(self, session_id):
        for key in self.connection.keys():
            if key.decode('utf-8') == session_id:
                return True
        return False


class Redis(DependencyProvider):
    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        self.connection_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

    def get_dependency(self, worker_ctx):
        return RedisWrapper(redis.Redis(connection_pool=self.connection_pool))

    def __del__(self):
        print("Redis Dependency Destructor")