# class Student:
#     classroom = '101'
#     address = 'beijing'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def print_age(cls):
#         print('%s: %s' % (cls.name, cls.age))

class A:
    def __init__(self, name):
        self.name = name
        print("父类的__init__方法被执行了！")

    def show(self):
        print("父类的show方法被执行了！")
        print(self.name)


class B(A):
    def __init__(self, name, age):
        # super().__init__(name=name)
        self.__age = age
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    def show(self):
        # super(B, self).show()
        print('子类的show方法被执行了 %s + %s' % (self.__age, self.__name))


if __name__ == '__main__':
    obj = B("jack", 18)
    print(obj.get_age())
    obj.set_age(66)
    print(obj.get_age())
    print(obj._B__age)
