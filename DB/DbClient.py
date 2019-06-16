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
            __type = "SsdbClient"
        else:
            pass
        assert __type, 'type error, Not supper DB type: {}'.format(config.db_type)
        # self.client = getattr(__import__(__type), 'ConnectionPool')(
        #     host=config.db_host,
        #     port=config.db_port,
        #     password=config.db_password,
        #     decode_responses=True,
        # )
        self.client = getattr(__import__(__type), __type)(
            name=config.db_name,
            host=config.db_host,
            port=config.db_port,
            password=config.db_password,
            decode_responses=True,
            db=0
        )

    def get(self, key, **kwargs):
        return self.client.get(key, *kwargs)

    def put(self, key, **kwargs):
        return self.client.put(key, **kwargs)

    def update(self, key, value, **kwargs):
        return self.client.update(key, value, **kwargs)

    def delete(self, key, **kwargs):
        return self.client.delete(self, key, **kwargs)

    def exists(self, key, **kwargs):
        return self.client.exists(key, **kwargs)

    def pop(self, **kwargs):
        return self.client.pop(**kwargs)

    def getAll(self):
        return self.client.getAll()

    def changeTable(self, name):
        self.client.changeTable(name)

    def getNumber(self):
        return self.client.getNumber()


if __name__ == '__main__':
    account = DbClient()
    # account.changeTable('useful_proxy')
    account.changeTable('map')
    print(account.get())
