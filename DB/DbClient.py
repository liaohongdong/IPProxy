import os
import time
import sys
import random
import redis

from Util.Print import o
from Config.ConfigGetter import config
from Util.utilClass import Singleton

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class DbClient(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.__initDbClient()

    def __initDbClient(self):
        __type = None
        if "redis" == config.db_type:
            __type = "redis"
        else:
            pass
        assert __type, 'type error, Not supper DB type: {}'.format(config.db_type)
        # self.client = getattr(__import__(__type), 'ConnectionPool')(
        #     host=config.db_host,
        #     port=config.db_port,
        #     password=config.db_password,
        #     decode_responses=True,
        # )
        pool = getattr(__import__(__type), 'ConnectionPool')(
            host=config.db_host,
            port=config.db_port,
            password=config.db_password,
            decode_responses=True,
            db=0
        )
        self.client = redis.Redis(connection_pool=pool)

    def get(self, key, *args):
        return self.client.hget(key, *args)
        # return self.client.hlen(key)

    def getFirst(self, *args):
        return self.client.hkeys(*args)[0]

    def getLast(self, *args):
        return self.client.hkeys(*args)[self.client.hlen(*args) - 1]

    def getRandom(self, *args):
        return random.choice(self.client.hkeys(*args))

    # def put(self, key, **kwargs):
    #     return self.client.put(key, **kwargs)

    def put(self, key, *args):
        return self.client.hset(key, *args)

    def delete(self, key, *args):
        return self.client.hdel(key, *args)

    def exists(self, key, *args):
        return self.client.hexists(key, *args)

    def getAll(self, key, *args):
        return self.client.hgetall(key)

    def getNumber(self):
        return self.client.dbsize()


if __name__ == '__main__':
    a = DbClient()
    a.put('map', "python", "123")
    # o(a.getNumber())
    # o(a.getAll('map'))
    # o(a.exists('map', 'python'))
    # o(a.delete('map', 'python'))
    # o(os.path.dirname(__file__))
    # o(__file__)
    # o(os.path.abspath(__file__))
    # o(os.path.dirname(os.path.abspath(__file__)))
    # print(__file__)
    # __type = False
    # assert __type, 'type error, Not supper DB type: {}'.format(config.db_type)

    # __type = "redis"
    # pool = getattr(__import__(__type), 'ConnectionPool')(
    #     host=config.db_host,
    #     port=config.db_port,
    #     password=config.db_password,
    #     decode_responses=True,
    # )
    # r = redis.Redis(connection_pool=pool)

    # r.mset({'a': 'a', 'a1': 'a1'})
    # print(r.mget('a', 'a1'))
    # r.getset('a', '1008611')
    # print(r.getrange('a', 0, 10))
    # r.setrange('a', 3, 'b')
    # r.setrange('a', 7, 4)
    # o(r.get('a'))
    # r.hset("hash1", "k13", "v122")
    # o(r.hgetall('hash1'))
    # r.rpush('liao', 1, 2, 3, 4)
    # o(r.lrange('liao', 0, r.llen('liao')))
    # o(r.strlen('a'))
    pass
