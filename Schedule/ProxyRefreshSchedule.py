import sys
import time
import logging
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler
from Util.utilFunction import validUsefulProxy
from Manager.ProxyManager import ProxyManager
from Util.LogHandler import Loghandler

sys.path.append('../')

logging.basicConfig()


class ProxyRefreshSchedule(ProxyManager):
    # 代理定时刷新、获取
    def __init__(self):
        ProxyManager.__init__(self)
        self.log = Loghandler('refresh_schedule')

    def validProxy(self):
        # 验证raw_proxy_queue中的代理, 将可用的代理放入useful_proxy_queue
        self.db.changeTable(self.raw_proxy_queue)
        try:
            raw_proxy_item, value = self.db.pop()
            self.log.info('ProxyRefreshSchedule: %s start validProxy' % time.ctime())
            # 计算剩余代理，用来减少重复计算
            # remaining_proxies = self.getAll()
            while raw_proxy_item:
                raw_proxy = raw_proxy_item
                if validUsefulProxy(raw_proxy):
                    self.db.changeTable(self.useful_proxy_queue)
                    self.db.put(value)
                    self.log.info('ProxyRefreshSchedule: %s validation pass' % raw_proxy)
                else:
                    self.log.info('ProxyRefreshSchedule: %s validation fail' % raw_proxy)

                self.db.changeTable(self.raw_proxy_queue)
                raw_proxy_item, value = self.db.pop()
                if raw_proxy_item is None:
                    break
                # remaining_proxies = self.getAll()
            self.log.info('ProxyRefreshSchedule: %s validProxy complete' % time.ctime())
        except Exception as e:
            # print(e)
            pass


def refreshPool():
    pp = ProxyRefreshSchedule()
    pp.validProxy()


def batchRefresh(process_num=30):
    # 检验新代理
    pl = []
    for num in range(process_num):
        proc = Thread(target=refreshPool, args=())
        pl.append(proc)

    for num in range(process_num):
        pl[num].daemon = True
        pl[num].start()

    for num in range(process_num):
        pl[num].join()


def fetchAll():
    p = ProxyRefreshSchedule()
    # 获取新代理
    p.refresh()


def run():
    scheduler = BackgroundScheduler()
    # 不用太快, 网站更新速度比较慢, 太快会加大验证压力, 导致raw_proxy积压
    scheduler.add_job(fetchAll, 'interval', minutes=10, id="fetch_proxy", max_instances=999999)
    # scheduler.add_job(batchRefresh, "interval", minutes=1)  # 每分钟检查一次
    scheduler.add_job(batchRefresh, "interval", seconds=10, max_instances=999999)  # 每分钟检查一次
    scheduler.start()

    fetchAll()

    while True:
        time.sleep(3)


if __name__ == '__main__':
    run()
