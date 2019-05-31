import sys
import pprint

PY3 = sys.version_info >= (3,)

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(sys.version_info)
