import time
import threading
import queue

q = queue.Queue(10)


def productor(i):
    while True:
        q.put("厨师 %s 做的包子！" % i)
        time.sleep(2)


def custom(j):
    while True:
        print("顾客 %s 吃了一个 %s" % (j, q.get()))
        time.sleep(1)


for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

for j in range(10):
    v = threading.Thread(target=custom, args=(j,))
    v.start()
