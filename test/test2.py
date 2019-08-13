import pprint
import math


class Cnm(object):
    def __init__(self):
        self.container = []
        self.i = 0

    def add(self, item):
        self.container.append(item)

    def __next__(self):
        if self.i < len(self.container):
            item = self.container[self.i]
            self.i += 1
            return item
        else:
            return StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    my_list1 = Cnm()

    my_list1.add(100)

    my_list1.add(200)

    my_list1.add(300)
    print(my_list1.container)

    it = my_list1.__iter__()

    from collections import Iterator

    print(isinstance(it, Iterator))

    for num in my_list1.container:
        print(num)

    # iterator =my_list1.__iter__()

    #

    # iterator.__next__() # 100  i=0

    # iterator.__next__() # 200  i=1

    #

    #

    # iterator2 =my_list1.__iter__()

    # iterator2.__next__() # 100   i=0
