import pprint as o


class test4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def gets(self):
        return self.age, self.name,


if __name__ == '__main__':
    # s = 'print("hhhha")'
    # d = compile(s, "<string>", 'exec')
    # print(d)
    # exec(d)

    # i = dir()
    # print(i)
    # ii = dir([1, 2])
    # print(ii)

    a = [1, 2, 3]
    # help(a)
    # print(locals())
    # print(globals())
    # v = memoryview(b'a1a2a3a4a5')
    # print(v[1:3])
    # print(bytes(v[1:3]))
    # print(vars())

    # li = [1, 2, 3]
    # data = map(lambda x: x * 100, li)
    # print(data)
    # print(type(data))
    # data = list(data)
    # print(data)

    # li = [11, 22, 33, 44, 55]
    # r = filter(lambda x: x > 33, li)
    # print(list(r))

    # a = [1, 2, 3]
    # b = ['a', 'b', 'c']
    # c = ['x', 'y', 'z']
    # d = zip(a, b, c)
    # print(list(d))

    # t = __import__("time")
    # o.pprint(t.gmtime())
    # o.pprint(t.__dict__)

    s = '愿圣光与你同在！\n\r' \
        '为了部落！\n\r' \
        '兽人永不为奴！\n\r' \
        '你们这是自寻死路！\n\r' \
        '复活吧我的勇士！\n\r' \
        '为你而战我的女士！\n\r'
    s = bytes(s, encoding='utf-8')
    o = open('./test.txt', mode='wb')
    o.write(s)
    o.close()

    # r = open('./test.txt', mode='rb')
    # z = r.readline()
    # z = z.decode('utf-8')
    # print(z)
    # z = r.readlines()
    # z = z.decode('utf-8')
    # print(z)

    # with open("./test.txt", "rb+") as f:
    #     f.write(b"1232312adsfalafds \n ")
    #     print(f.tell())
    #     f.seek(-8, 2)
    #     print(f.read(3))
    #     f.close()
