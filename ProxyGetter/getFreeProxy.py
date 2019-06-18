import re
import sys
import requests
import time
import json

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
                    arr = ul.xpath('.//li/text()')
                    yield {
                        'ip': arr[0],  # 地址
                        'port': arr[1],  # 端口
                        'anonymity': arr[2],  # 透明度
                        'type': arr[3],  # 网络类型
                        'country': arr[4],  # 国家
                        'province': arr[5],  # 省市
                        'operator': arr[6],  # 运营商
                        'resp_speed': arr[7],  # 响应速度
                        'final_verify_time': arr[8],  # 最后验证时间
                        'life': '',  # 存活时间
                    }
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
        }
        for index, _ in enumerate(urls):
            url = _.format(count=count)
            page = cls.driver(url, headers)
            ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}", page)
            for item in ips:
                arr = item.split(':')
                yield {
                    'ip': arr[0],  # 地址
                    'port': arr[1],  # 端口
                    'anonymity': '',  # 透明度
                    'type': '',  # 网络类型
                    'country': '',  # 国家
                    'province': '',  # 省市
                    'operator': '',  # 运营商
                    'resp_speed': '',  # 响应速度
                    'final_verify_time': '',  # 最后验证时间
                    'life': '',  # 存活时间
                }

    @staticmethod  # 有点用不了 网站打开很慢
    def freeProxyThird():
        url = 'http://www.ip181.com/'
        # html_tree = getHtmlTree(url)
        resp = requests.get(url, timeout=30)
        html_tree = resp.content
        try:
            jsonstr = json.loads(html_tree.decode('utf-8'))
            result = jsonstr['RESULT']
            for i in result:
                yield {
                    'ip': i['ip'],  # 地址
                    'port': i['port'],  # 端口
                    'anonymity': '',  # 透明度
                    'type': '',  # 网络类型
                    'country': '',  # 国家
                    'province': i['position'],  # 省市
                    'operator': '',  # 运营商
                    'resp_speed': '',  # 响应速度
                    'final_verify_time': '',  # 最后验证时间
                    'life': '',  # 存活时间
                }
        except Exception as e:
            pass

    @staticmethod
    def freeProxyFourth(page_count=1):
        url_list = [
            'http://www.xicidaili.com/nn/',  # 高匿
            'http://www.xicidaili.com/nt/',  # 透明
            'https://www.xicidaili.com/wn/',  # https
            'https://www.xicidaili.com/wt/',  # http
        ]
        for each_url in url_list:
            for i in range(1, page_count + 1):
                url = each_url + str(i)
                tree = getHtmlTree(url)
                proxy_list = tree.xpath('.//table[@id="ip_list"]//tr[position()>1]')
                for proxy in proxy_list:
                    try:
                        ip = proxy.xpath('./td[2]/text()')
                        port = proxy.xpath('./td[3]/text()')
                        province = proxy.xpath('./td[4]/a/text()')
                        anonymity = proxy.xpath('./td[5]/text()')
                        type = proxy.xpath('./td[6]/text()')
                        resp_speed = proxy.xpath('./td[7]/div[1]/@title')
                        life = proxy.xpath('./td[9]/text()')
                        final_verify_time = proxy.xpath('./td[10]/text()')
                        # o(ip+port+province+anonymity+type+resp_speed+left+final_verify_time)
                        yield {
                            'ip': ip[0],  # 地址
                            'port': port[0],  # 端口
                            'anonymity': anonymity[0],  # 透明度
                            'type': type[0],  # 网络类型
                            'country': '',  # 国家
                            'province': province[0],  # 省市
                            'operator': '',  # 运营商
                            'resp_speed': resp_speed[0],  # 响应速度
                            'final_verify_time': final_verify_time[0],  # 最后验证时间
                            'life': life[0],  # 存活时间
                        }
                    except Exception as e:
                        o(e)

    @staticmethod
    def freeProxyFifth():
        url = "http://www.goubanjia.com/"

    @staticmethod
    def driver(url, headers):
        # print(url)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('user-agent=' + headers['User-Agent'])
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        driver.get(url)
        cookies_clearance = driver.get_cookie('__jsl_clearance')
        cookies_jsluid = driver.get_cookie('__jsluid')
        # o(cookies_clearance)
        # o(cookies_jsluid)
        driver.delete_all_cookies()
        driver.add_cookie({'name': '__jsl_clearance', 'value': cookies_clearance['value']})
        driver.add_cookie({'name': '__jsluid', 'value': cookies_jsluid['value']})
        driver.get(url)
        driver.implicitly_wait(1)
        driver.maximize_window()
        time.sleep(1)
        html = driver.page_source
        return html
        # o(html)
        # open(str(time.gmtime().tm_sec) + 'a.html', 'w').write(html)
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
    # d = g.freeProxySecond()
    # d = g.freeProxyThird()
    # d = g.freeProxyFourth()
    d = g.freeProxyFifth()
    for i in d:
        o(i)
