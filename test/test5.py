import pprint as o
import threading as t
import time


# def doWaiting():
#     print('start waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))
#
#
# def run():
#     print(t.current_thread().getName(), "开始工作")
#     time.sleep(2)
#     print("子线程工作完毕")
#
#
# for i in range(3):
#     d = t.Thread(target=run)
#     d.setDaemon(True)
#     d.start()


class MyThreading(t.Thread):
    def __init__(self, func, arg):
        super().__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)


def my_fun(e):
    print('dd', e)
    time.sleep(3)
    print('ss', e)


if __name__ == '__main__':
    # s = t.Thread(target=doWaiting)
    # s.start()
    # time.sleep(1)
    # print('start job')
    # s.join()
    # print('end job')

    # time.sleep(1)
    # print("主线程结束")
    # print(t.active_count())

    o = MyThreading(my_fun, 222)
    o.start()
