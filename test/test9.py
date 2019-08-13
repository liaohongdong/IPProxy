# from multiprocessing import Pool
# import time
#
#
# def func(args):
#     time.sleep(1)
#     print("正在执行进程 ", args)
#
#
# if __name__ == '__main__':
#
#     p = Pool(5)  # 创建一个包含5个进程的进程池
#
#     for i in range(30):
#         p.apply_async(func=func, args=(i,))
#
#     p.close()  # 等子进程执行完毕后关闭进程池
#     # time.sleep(2)
#     # p.terminate()     # 立刻关闭进程池
#     p.join()


import time
#
#
# def task1():
#     while True:
#         yield "<甲>也累了，让<乙>工作一会儿"
#         time.sleep(1)
#         print("<甲>工作了一段时间.....")
#
#
# def task2(t):
#     next(t)
#     while True:
#         print("-----------------------------------")
#         print("<乙>工作了一段时间.....")
#         time.sleep(2)
#         print("<乙>累了，让<甲>工作一会儿....")
#         ret = t.send(None)
#         print(ret)
#     t.close()
#
#
# if __name__ == '__main__':
#     t = task1()
#     task2(t)


# def simple_coroutine():
#     print('-> 启动协程')
#     y = 10
#     x = yield y
#     print('-> 协程接收到了x的值:', x)
#
#
# my_coro = simple_coroutine()
# ret = next(my_coro)
# print(ret)
# time.sleep(5)
# my_coro.send(10)


# import asyncio
# import datetime
#
#
# async def display_date(num, loop):  # 注意这一行的写法
#     end_time = loop.time() + 10.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果
#         print('继续执行')
#
#
# loop = asyncio.get_event_loop()  # 获取一个event_loop
# tasks = [display_date(1, loop), display_date(2, loop)]
# loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
# print(111223)


# import asyncio
#
#
# async def func(future):
#     await asyncio.sleep(5)
#     future.set_result('Future is done!')
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     future = asyncio.Future()
#     asyncio.ensure_future(func(future))
#     print(loop.is_running(), 2)  # 查看当前状态时循环是否已经启动
#     loop.run_until_complete(future)
#     print(future.result(), 3)
#     loop.close()


import asyncio


async def func(future):
    await asyncio.sleep(5)
    future.set_result('Future is done!')


def call_result(future):
    print(future.result())
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    future.add_done_callback(call_result)  # 注意这行
    try:
        loop.run_forever()
    finally:
        loop.close()
