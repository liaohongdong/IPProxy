import requests
# from test import testRun

if __name__ == '__main__':
    asd = '124.207.82.166:8008'
    # d = requests.get('http://www.baidu.com/', proxies={"http": "http://111.13.134.22:80"}, timeout=10)
    d = requests.get('http://www.baidu.com/', proxies={"http": asd}, timeout=15)
    print(d)
    d1 = requests.get("http://httpbin.org/ip", proxies={"http": asd}, timeout=15, verify=False)
    print(d1)
    # 16:21:47
    # t = testRun()
