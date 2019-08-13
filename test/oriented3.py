if __name__ == '__main__':
    sex = int(input("Please input a number: "))

    try:
        if sex == 1:
            print("这是个男人！")
        elif sex == 0:
            print("这是个女人！")
        else:
            print("好像有什么不符合常理的事情发生了！！")
    except Exception as e:
        print(1)
    finally:
        print('finally')

    # except ValueError:
    # print("这是个人妖！")

    import sys
    import time


    def bar(num, total):
        rate = num / total
        rate_num = int(rate * 100)
        r = '\r[%s%s]%d%%' % ("=" * num, " " * (100 - num), rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush()


    if __name__ == '__main__':
        for i in range(0, 101):
            time.sleep(0.1)
            bar(i, 100)