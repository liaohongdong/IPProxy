import re
import sys
import requests

from Util.Print import o
from Util.utilFunction import getHtmlTree
from Util.WebRequest import WebRequest
from selenium import webdriver

sys.path.append('..')

requests.packages.urllib3.disable_warnings()


class GetFreeProxy(object):
    @staticmethod
    def freeProxyFirst(page=10):
        url_list = [
            'http://www.data5u.com/',
            # 'http://www.data5u.com/free/gngn/index.shtml',
            # 'http://www.data5u.com/free/gnpt/index.shtml'
        ]
        for url in url_list:
            html_tree = getHtmlTree(url)
            ul_list = html_tree.xpath('//ul[@class="l2"]')
            for ul in ul_list:
                try:
                    yield ':'.join(ul.xpath('.//li/text()')[0:2])
                except Exception as e:
                    print(e)

    @staticmethod
    def freeProxySecond(count=20):
        urls = [
            "http://www.66ip.cn/mo.php?sxb=&tqsl={count}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=",
            "http://www.66ip.cn/nmtq.php?getnum={count}&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip",
        ]
        request = WebRequest()
        url = urls[0].format(count=count)
        o(url)
        html = request.get(url).content
        o(html.decode('utf8'))
        return
        for _ in urls:
            url = _.format(count=count)
            html = request.get(url).content
            o(html)
            ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}", html.decode('utf-8'))
            # o(ips)
            # for ip in ips:
            #     ip = ip.decode('utf-8')
            #     print(ip.strip())
            #     yield ip.strip()

    @staticmethod
    def driver():
        d = webdriver.Chrome()
        d.get('http://www.baidu.com')
        d.find_element_by_id('kw').send_keys('selenium')
        d.find_element_by_id('su').click()
        

if __name__ == '__main__':
    g = GetFreeProxy()
    # d = g.freeProxyFirst()
    # g.freeProxySecond()
    g.driver()

    # for i in d:
    #     o(i)
