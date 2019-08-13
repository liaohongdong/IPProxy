import threading as td
from threading import Timer
import time as t

number = 0
lock = td.Lock()


def hello():
    print("hello, world")


def plug(lk):
    global number
    with lk:
        for _ in range(1000000):
            number += 1
        print("子线程%s运算结束后，number = %s" % (td.current_thread().getName(), number))
        # print("run the thread: %s" % n)


if __name__ == '__main__':
    semaphore = td.BoundedSemaphore(1)
    for i in range(6):
        d = td.Thread(target=plug, args=(lock,))
        # d = td.Thread(target=plug, args=(i, semaphore))
        d.start()

    ts = Timer(3, hello)
    ts.start()
    # t.sleep(2)
    # print("主线程执行完毕后，number = ", number)
