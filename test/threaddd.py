import time
import queue
import threading


def aaa(i):
    while True:
        item = q.get()
        if item is None:
            print("线程%s发现了一个None,可以休息了^-^" % i)
            break
        time.sleep(0.01)
        print('aaaaa -> ' + str(i) + " ---> " + str(item))
        q.task_done()


if __name__ == '__main__':
    num_of_threads = 5
    source = [i for i in range(1, 21)]
    q = queue.Queue()
    threads = []
    for i in range(1, num_of_threads + 1):
        t = threading.Thread(target=aaa, args=(i,))
        threads.append(t)
        t.start()

    for item in source:
        time.sleep(0.01)
        q.put(item)

    q.join()
    # print("-----工作都完成了-----")
    # # 停止工作线程
    for i in range(num_of_threads):
        q.put(None)
    # for t in threads:
    #     t.join()
    # print(threads)
