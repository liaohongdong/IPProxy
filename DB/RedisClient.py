import random
import redis
import json
import sys
from Util.Print import o


class RedisClient(object):
    def __init__(self, name, host, port, username=None, **kwargs):
        self.name = name
        self.__conn = redis.Redis(host=host, port=port, socket_timeout=30, **kwargs)

    def get(self):
        key = self.__conn.hgetall(name=self.name)
        rkey = random.choice(list(key.keys())) if key else None
        if rkey is not None:
            return rkey, self.getvalue(rkey)
        else:
            return None

    def put(self, key):
        if type(key) == str:
            try:
                key = json.loads(key)
            except Exception as e:
                pass
        key = key if isinstance(key, dict) else key

        return self.__conn.hset(self.name, key['ip'] + ':' + key['port'], json.dumps(key))

    def getvalue(self, key):
        value = self.__conn.hget(self.name, key)
        return value if value else None

    def pop(self):
        try:
            key, value = self.get()
            if key:
                self.__conn.hdel(self.name, key)
            return key, value
        except Exception as e:
            # print(e)
            pass

    def delete(self, key):
        self.__conn.hdel(self.name, key)

    def inckey(self, key, value):
        self.__conn.hincrby(self.name, key, value)

    def getAll(self):
        # if sys.version_info.major == 3:
        return [key for key in self.__conn.hgetall(self.name).keys()]
        # else:
        #     return self.__conn.hlen(self.name)

    def getAllDict(self):
        return self.__conn.hgetall(self.name)

    def getNumber(self, *args):
        print(args)
        self.changeTable(args[0])
        raw = self.getAll()
        self.changeTable(args[1])
        useful = self.getAll()
        return len(raw), len(useful)

    def changeTable(self, name):
        self.name = name


if __name__ == '__main__':
    r = RedisClient('', '39.108.115.177', 6379)
    r.changeTable('raw_proxy')
    o(r.getAll())
    # o(r.get())
    pass
