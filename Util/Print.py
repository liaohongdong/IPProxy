import pprint


class Out(object):
    def __init__(self):
        pass

    def o(slef, info=''):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(info)


o = Out().o
