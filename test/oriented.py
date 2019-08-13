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

class People:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


class student(People):

    def __init__(self, name, age, weight, grade):
        # 调用父类的实例化方法
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的speak方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


if __name__ == '__main__':
    s = student('ken', 10, 30, 3)
    s.speak()
