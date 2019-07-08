import sys
import json
from threading import Thread
from Util.utilFunction import validUsefulProxy
from Manager.ProxyManager import ProxyManager
from Util.LogHandler import Loghandler
from Util.Print import o

sys.path.append('../')

FAIL_COUNT = 1  # 检验失败次数，超过次数删除代理

from queue import Queue  # py2


class ProxyCheck(ProxyManager, Thread):
    def __init__(self, queue, item_dict):
        # def __init__(self):
        ProxyManager.__init__(self)
        Thread.__init__(self)
        self.log = Loghandler('proxy_check', file=False)  # 多线程同时写一个日志文件会有问题
        self.queue = queue
        self.item_dict = item_dict

        # self.queue = Queue()
        # self.item_dict = dict()

    def run(self):
        self.db.changeTable(self.useful_proxy_queue)
        # self.putQueue()
        while self.queue.qsize:
            proxy = self.queue.get()
            # o(proxy)
            # o(json.loads(self.item_dict[proxy['ip']+':'+proxy['port']]))
            count = proxy['num']
            name = proxy['ip'] + ':' + proxy['port']
            if validUsefulProxy(name):
                # 验证通过计数器减1
                # if count and int(count) > 0:
                #     self.db.put(proxy, num=int(count) - 1)
                # else:
                #     pass
                # self.log.info('ProxyCheck: {} validation pass'.format(proxy))
                pass
            else:
                self.log.info('ProxyCheck: {} validation fail'.format(proxy))
                if count and int(count) < FAIL_COUNT:
                    self.log.info('ProxyCheck: {} fail too many, delete!'.format(proxy))
                    self.db.delete(name)
                else:
                    proxy['num'] = int(count) - 1
                    self.db.put(proxy)
            self.queue.task_done()

    # def putQueue(self):
    #     self.db.changeTable(self.useful_proxy_queue)
    #     self.item_dict = self.db.getAllDict()
    #     for item in self.item_dict:
    #         self.queue.put(json.loads(self.item_dict[item]))


if __name__ == '__main__':
    p = ProxyCheck()
    p.run()
    pass
