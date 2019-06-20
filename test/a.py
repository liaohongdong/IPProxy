import time
import json

if __name__ == '__main__':
    # a = 10
    # while '39.108.111.222:1080':
    #     a -= 1
    #     print(a)
    #     if a <= 0:
    #         break
    # a = ['a', 'b', 'c', 'd']
    # a = []
    # while a:
    #     print(time.gmtime().tm_sec)
    #     time.sleep(3)
    a = {'d': 'd', 'c': 'c'}
    print(json.dumps(a))
    q = '{"d": "d", "c": "c"}'
    aa = json.loads(q)
    print(aa['c'])
