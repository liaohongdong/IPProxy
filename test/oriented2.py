class People:
    '''123123nikanzhege wendang
    '''

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age3(self):
        return self.__age

    @age3.setter
    def age1(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @age3.deleter
    def age2(self):
        print("删除年龄数据！")

    def __str__(self):
        return '__str__'

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __del__(self):
        print('销毁了~~~~~')


if __name__ == '__main__':
    obj = People("jack", 18)
    print(obj)
    obj()
    print(obj.age3)
    obj.age1 = 19
    print("obj.age:  ", obj.age3)
    del obj.age2
    print(obj.__doc__)
    print(obj.__module__)
    print(obj.__class__)
    print(obj.__dict__)
    del obj
