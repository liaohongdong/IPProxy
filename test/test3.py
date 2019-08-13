if __name__ == '__main__':
    # def fibonacci(n):
    #     a, b, counter = 0, 1, 0
    #     while True:
    #         if counter > n:
    #             return
    #         yield a
    #         a, b = b, a + b
    #         counter += 1
    #
    #
    # f = fibonacci(10)
    # print(f)
    # for i in f:
    #     print(i)

    def outer(func):
        def inner():
            print("认证成功！")
            result = func()
            print("日志添加成功")
            return result

        return inner


    def outer2(func):
        def inner():
            print("欢迎1")
            result = func()
            print("欢迎2")
            return result

        return inner

    @outer2
    @outer
    def f1():
        print("业务部门1的数据接口......")


    @outer2
    @outer
    def f2():
        print("业务部门2的数据接口......")


    @outer2
    @outer
    def f3():
        print("业务部门3的数据接口......")


    @outer2
    @outer
    def f100():
        print("业务部门100的数据接口......")


    # 各部门分别调用自己需要的API
    f1()
    f2()
    f3()
    f100()
