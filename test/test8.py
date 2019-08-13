# import os
# import multiprocessing
#
#
# def foo(i):
#     # 同样的参数传递方法
#     print("这里是 ", multiprocessing.current_process().name)
#     print('模块名称:', __name__)
#     print('父进程 id:', os.getppid())  # 获取父进程id
#     print('当前子进程 id:', os.getpid())  # 获取自己的进程id
#     print('------------------------')
#
#
# if __name__ == '__main__':
#
#     for i in range(50):
#         p = multiprocessing.Process(target=foo, args=(i,))
#         p.start()

# from multiprocessing import Process
#
# lis = []
#
#
# def foo(i):
#     lis.append(i)
#     lis.append(i)
#     __import__('pprint').pprint(lis)
#     print("This is Process ", i, " and lis is ", lis, " and lis.address is  ", id(lis))
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = Process(target=foo, args=(i,))
#         p.start()
#
#     p.join()
#     print("The end of list_1:", lis)

from multiprocessing import Process
from multiprocessing import Manager


def func(i, dic):
    # dic.insert(i, 100 + i)
    dic[i] = 100 + i
    print(dic)


if __name__ == '__main__':
    dic = Manager().dict()
    # dic = Manager().list()
    for i in range(10):
        p = Process(target=func, args=(i, dic))
        p.start()
        p.join()
    print(dic)
