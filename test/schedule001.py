# from apscheduler.schedulers.blocking import BlockingScheduler
# import time
#
# scheduler = BlockingScheduler()
#
#
# @scheduler.scheduled_job('interval', seconds=3)
# def job1():
#     print("%s: 执行任务" % time.asctime())
#
#
# # scheduler.add_job(job1, 'interval', seconds=3)
# scheduler.start()

from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler()


def job1():
    print("%s: 执行任务" % time.asctime())


scheduler.add_job(job1, 'interval', seconds=3)
scheduler.start()

while True:
    pass
