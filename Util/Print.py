import pprint

class out():
    def __init__(self, info=""):
        self.pp = pprint.PrettyPrinter(indent=4)
        self.pp.pprint(info)

