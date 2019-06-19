import json
import random
import redis
import sys
from Util.Print import o


class RedisClient(object):
    def __init__(self, name, host, port, username=None, **kwargs):
        self.name = name
        self.__conn = redis.Redis(host=host, port=port, socket_timeout=30, **kwargs)

    def get(self):
        key = self.__conn.hgetall(name=self.name)
        rkey = random.choice(list(key.keys())) if key else None
        if isinstance(rkey, bytes):
            return rkey.decode('utf-8')
        else:
            return rkey

    def put(self, key):
        key = key if isinstance(key, dict) else key
        return self.__conn.hset(self.name, key['ip'] + key['port'], json.dumps(key))

    def getvalue(self, key):
        value = self.__conn.hget(self.name, key)
        return value if value else None

    def pop(self):
        key = self.get()
        if key:
            self.__conn.hdel(self.name, key)
        return key

    def delete(self, key):
        self.__conn.hdel(self.name, key)

    def inckey(self, key, value):
        self.__conn.hincrby(self.name, key, value)

    def getAll(self):
        if sys.version_info.major == 3:
            return [key.decode('utf-8') for key in self.__conn.hgetall(self.name).keys()]
        else:
            return self.__conn.hlen(self.name)

    def changeTable(self, name):
        self.name = name


if __name__ == '__main__':
    r = RedisClient('', '39.108.115.177', 6379)
    r.changeTable('map')
    o(r.get())
    pass
