import sys
import json
import time

try:
    from Queue import Queue  # py3
except:
    from queue import Queue  # py2

sys.path.append('../')

from Schedule.ProxyCheck import ProxyCheck
from Manager.ProxyManager import ProxyManager


class ProxyValidSchedule(ProxyManager, object):
    def __init__(self):
        ProxyManager.__init__(self)
        self.queue = Queue()
        self.proxy_item = dict()

    def __validProxy(self, threads=20):
        # 验证useful_proxy代理
        thread_list = list()
        for index in range(threads):
            thread_list.append(ProxyCheck(self.queue, self.proxy_item))

        for thread in thread_list:
            thread.daemon = True
            thread.start()

        for thread in thread_list:
            thread.join()

    def main(self):
        self.putQueue()
        while True:
            if not self.queue.empty():
                self.log.info("Start valid useful proxy")
                self.__validProxy()
            else:
                self.log.info('Valid Complete! sleep 5 sec.')
                time.sleep(5)
                self.putQueue()

    def putQueue(self):
        self.db.changeTable(self.useful_proxy_queue)
        self.proxy_item = self.db.getAllDict()
        for item in self.proxy_item:
            self.queue.put(json.loads(self.proxy_item[item]))


def run():
    pp = ProxyValidSchedule()
    pp.main()


if __name__ == '__main__':
    p = ProxyValidSchedule()
    p.main()
