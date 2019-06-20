import requests
import time
from lxml import etree

from Util.LogHandler import Loghandler
from Util.WebRequest import WebRequest
import re

from socket import socket, AF_INET, SOCK_STREAM


def robustCrawl(func):
    def decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            pass

    return decorate


def verifyProxyFormat(proxy):
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    _proxy = re.findall(verify_regex, proxy['ip'])
    return True if len(_proxy) == 1 else False


def getHtmlTree(url, **kwargs):
    header = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    wr = WebRequest()
    time.sleep(2)
    html = wr.get(url=url, header=header).content
    return etree.HTML(html)


def tcpConnent(proxy):
    s = socket(AF_INET, SOCK_STREAM)
    ip, port = proxy.split(':')
    result = s.connect_ex(ip, int(port))
    return True if result == 0 else False


def validUsefulProxy(proxy):
    proxies = {
        "http": "http://{proxy}".format(proxy=proxy)
        # "http": "82.114.241.138:8080"
    }
    try:
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=15, verify=False)
        print(r.status_code)
        if r.status_code == 200 and r.json().get("origin"):
            return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    validUsefulProxy('1')
    pass
