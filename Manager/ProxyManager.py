import random
from Util import EnvUtil
from DB.DbClient import DbClient
from Config.ConfigGetter import config
from Util.LogHandler import Loghandler
from Util.utilFunction import verifyProxyFormat
from ProxyGetter.getFreeProxy import GetFreeProxy


class ProxyManager(object):

    def __init__(self):
        self.db = DbClient()
        self.raw_proxy_queue = 'raw_proxy'
        self.log = Loghandler('proxy_manager')
        self.useful_proxy_queue = 'useful_proxy'

    def refresh(self):
        self.db.changeTable(self.raw_proxy_queue)
        for proxyGetter in config.proxy_getter_functions:
            try:
                self.log.info("{func}: fetch proxy start".format(func=proxyGetter))
                for proxy in getattr(GetFreeProxy, proxyGetter.strip())():
                    if proxy is not False:
                        if proxy and verifyProxyFormat(proxy):
                            self.log.info("{func}: fetch proxy {proxy}".format(func=proxyGetter, proxy=proxy))
                            self.db.put(proxy)
                        else:
                            self.log.error("{func}: fetch proxy {proxy} error".format(func=proxyGetter, proxy=proxy))
            except Exception as s:
                self.log.error("refresh: {}".format(s))
                self.log.error("{func}: fetch proxy fail".format(func=proxyGetter))
                continue

    def get(self):
        self.db.changeTable(self.useful_proxy_queue)
        item_dict = self.db.getAll()
        if item_dict:
            if EnvUtil.PY3:
                return random.choice(list(item_dict.keys()))
            else:
                return random.choice(item_dict.keys())
        return None

    def delete(self, proxy):
        self.db.changeTable(self.useful_proxy_queue)
        self.db.delete(proxy)

    def getAll(self):
        # self.db.changeTable(self.useful_proxy_queue)
        return self.db.getAll()
        # if EnvUtil.PY3:
        #     return list(item_dict.keys()) if item_dict else list()
        # return item_dict.keys() if item_dict else list()

    def getNumber(self):
        self.db.changeTable(self.raw_proxy_queue)
        total_raw_proxy = self.db.getNumber()
        self.db.changeTable(self.useful_proxy_queue)
        total_useful_proxy = self.db.getNumber()
        return {
            'raw_proxy': total_raw_proxy,
            'useful_proxy': total_useful_proxy
        }


if __name__ == '__main__':
    p = ProxyManager()
    p.refresh()
