from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler
import time


# scheduler = BackgroundScheduler()
#
#
# def job1():
#     print("%s: 执行任务" % time.asctime())
#
#
# scheduler.add_job(job1, 'interval', seconds=3, max_instances=5)
# scheduler.start()
#
# while True:
#     time.sleep(30)
class schedule002(object):
    def __init__(self):
        self.i = 1

    def ggg(self, p):
        while True:
            if self.i >= 10:
                break
            print('ggg', self.i, p)
            self.i += 1
            time.sleep(1)


def pool(p):
    s = schedule002()
    s.ggg(p)


def thed(p=30):
    pl = []
    for num in range(p):
        proc = Thread(target=pool, args=(num,))
        pl.append(proc)

    for num in range(p):
        pl[num].daemon = True
        pl[num].start()

    for num in range(p):
        pl[num].join()


def run():
    schedule = BackgroundScheduler()
    schedule.add_job(thed, 'interval', seconds=20, id='liao', max_instances=3)
    schedule.start()

    while True:
        time.sleep(30)


if __name__ == '__main__':
    # thed()
    # pool()
    run()
