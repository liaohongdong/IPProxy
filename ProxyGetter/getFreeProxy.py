import re
import sys
import requests
import time
from Util.Print import o
from Util.utilFunction import getHtmlTree
from Util.WebRequest import WebRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree

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

    @classmethod
    def freeProxySecond(cls, count=20):
        urls = [
            "http://www.66ip.cn/mo.php?sxb=&tqsl={count}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=",
            "http://www.66ip.cn/nmtq.php?getnum={count}&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip",
        ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Cookie': '__jsluid=791a40e3ae570ed6fcbe6ae547617390; __jsl_clearance=1560760725.943|0|LZc2w%2FdLv49feXKKfnYUm4SIy1s%3D'
        }
        for index, _ in enumerate(urls):
            url = _.format(count=count)
            cls.driver(url, headers)

            # html = request.get(url).content
            # ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}", html.decode('utf-8'))
            # o(ips)
            # for ip in ips:
            #     ip = ip.decode('utf-8')
            #     print(ip.strip())
            #     yield ip.strip()

    @staticmethod
    def driver(url, headers):
        print(url)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('user-agent=' + headers['User-Agent'])
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        driver.get(url)
        cookies_clearance = driver.get_cookie('__jsl_clearance')
        cookies_jsluid = driver.get_cookie('__jsluid')
        driver.delete_all_cookies()
        driver.add_cookie({'name': '__jsl_clearance', 'value': cookies_clearance['value']})
        driver.add_cookie({'name': '__jsluid', 'value': cookies_jsluid['value']})

        driver.get(url)
        driver.implicitly_wait(1)
        driver.maximize_window()
        time.sleep(1)
        html = driver.page_source
        open(str(time.gmtime().tm_sec) + 'a.html', 'w').write(html)
        # -------------------------------------- #
        # d.get('http://www.baidu.com')
        # d.implicitly_wait(1)
        # d.maximize_window()
        # d.find_element_by_id('kw').send_keys('selenium')
        # d.find_element_by_id('su').click()
        # time.sleep(1)
        # html = d.page_source
        # open('aaa.html', 'w').write(html)
        # dom = etree.HTML(html)
        # left = dom.xpath('//div[@id="content_left"]/*[@class="result c-container "]')
        # for i in left:
        #     o(i.xpath('./h3/a/@href'))
        # print(len(left))
        # print(type(dom))
        # -------------------------------------- #


if __name__ == '__main__':
    g = GetFreeProxy()
    # d = g.freeProxyFirst()
    # g.freeProxySecond()
    # g.driver()
    g.freeProxySecond()

    # for i in d:
    #     o(i)
