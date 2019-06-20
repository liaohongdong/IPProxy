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
    @classmethod
    def freeProxyFirst(cls, page=10):
        url_list = [
            'http://www.data5u.com/',
            # 'http://www.data5u.com/free/gngn/index.shtml',
            # 'http://www.data5u.com/free/gnpt/index.shtml'
        ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }
        for url in url_list:
            # html_tree = getHtmlTree(url)
            page = cls.driver(url, headers)
            html_tree = etree.HTML(page)
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
                        'num': 3
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
            page = cls.driver(url, headers, cookie=True)
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
                    'num': 3
                }

    @classmethod  # 有点用不了 网站打开很慢
    def freeProxyThird(cls):
        url = 'http://www.ip181.com/'
        # html_tree = getHtmlTree(url)
        resp = requests.get(url, timeout=60)
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
                    'num': 3
                }
        except Exception as e:
            pass

    @classmethod
    def freeProxyFourth(cls, page_count=1):
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
                        types = proxy.xpath('./td[6]/text()')
                        resp_speed = proxy.xpath('./td[7]/div[1]/@title')
                        life = proxy.xpath('./td[9]/text()')
                        final_verify_time = proxy.xpath('./td[10]/text()')
                        # o(ip+port+province+anonymity+type+resp_speed+left+final_verify_time)
                        yield {
                            'ip': ip[0],  # 地址
                            'port': port[0],  # 端口
                            'anonymity': anonymity[0],  # 透明度
                            'type': types[0],  # 网络类型
                            'country': '',  # 国家
                            'province': province[0],  # 省市
                            'operator': '',  # 运营商
                            'resp_speed': resp_speed[0],  # 响应速度
                            'final_verify_time': final_verify_time[0],  # 最后验证时间
                            'life': life[0],  # 存活时间
                            'num': 3
                        }
                    except Exception as e:
                        o(e)

    @classmethod
    def freeProxyFifth(cls):
        url = "http://www.goubanjia.com/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }
        page = cls.driver(url, headers)
        proxy_list = etree.HTML(page).xpath('//td[@class="ip"]')
        # 此网站有隐藏的数字干扰，或抓取到多余的数字或.符号
        # 需要过滤掉<p style="display:none;">的内容
        xpath_str = """.//*[not(contains(@style, 'display: none'))
                            and not(contains(@style, 'display:none'))
                            and not(contains(@class, 'port'))
                            ]/text()
                    """
        for each_proxy in proxy_list:
            try:
                # :符号裸放在td下，其他放在div span p中，先分割找出ip，再找port
                ip_addr = ''.join(each_proxy.xpath(xpath_str))
                port = each_proxy.xpath(".//span[contains(@class, 'port')]/text()")[0]
                anonymity = each_proxy.xpath(".//../td[2]/a/text()")
                types = each_proxy.xpath(".//../td[3]/a/text()")[0]
                address = each_proxy.xpath(".//../td[4]/a/text()")
                country = address[0]
                province = address[1] + address[2]
                operator = each_proxy.xpath(".//../td[5]/a/text()")[0]
                resp_speed = each_proxy.xpath(".//../td[6]/text()")[0]
                final_verify_time = each_proxy.xpath(".//../td[7]/text()")[0]
                life = each_proxy.xpath(".//../td[8]/text()")[0]
                yield {
                    'ip': ip_addr,  # 地址
                    'port': port,  # 端口
                    'anonymity': anonymity[0],  # 透明度
                    'type': types,  # 网络类型
                    'country': country,  # 国家
                    'province': province,  # 省市
                    'operator': operator,  # 运营商
                    'resp_speed': resp_speed,  # 响应速度
                    'final_verify_time': final_verify_time,  # 最后验证时间
                    'life': life,  # 存活时间
                    'num': 3
                }
            except Exception as e:
                o(e)

    @classmethod
    def freeProxySixth(cls):
        url_list = [
            'https://www.kuaidaili.com/free/inha/',
            'https://www.kuaidaili.com/free/intr/'
        ]
        for url in url_list:
            tree = getHtmlTree(url)
            proxy_list = tree.xpath('.//table//tr')
            for tr in proxy_list[1:]:
                # yield ':'.join(tr.xpath('./td/text()')[0:2])
                yield {
                    'ip': tr.xpath('./td[1]/text()')[0],  # 地址
                    'port': tr.xpath('./td[2]/text()')[0],  # 端口
                    'anonymity': tr.xpath('./td[3]/text()')[0],  # 透明度
                    'type': tr.xpath('./td[4]/text()')[0],  # 网络类型
                    'country': '',  # 国家
                    'province': tr.xpath('./td[5]/text()')[0],  # 省市
                    'operator': '',  # 运营商
                    'resp_speed': tr.xpath('./td[6]/text()')[0],  # 响应速度
                    'final_verify_time': tr.xpath('./td[7]/text()')[0],  # 最后验证时间
                    'life': '',  # 存活时间
                    'num': 3
                }

    @classmethod
    def freeProxySeventh(cls):
        """
        云代理 http://www.ip3366.net/free/
        """
        urls = ['http://www.ip3366.net/free/']
        request = WebRequest()
        for url in urls:
            r = request.get(url, timeout=10)
            page = r.content.decode('utf-8', 'ignore')
            html = etree.HTML(page)
            tr_list = html.xpath('.//table/tbody/tr')
            for il in tr_list:
                # o(il.xpath('.//td[1]/text()')+il.xpath('.//td[2]/text()'))
                yield {
                    'ip': il.xpath('.//td[1]/text()')[0],  # 地址
                    'port': il.xpath('.//td[2]/text()')[0],  # 端口
                    'anonymity': '',  # 透明度
                    'type': il.xpath('.//td[4]/text()')[0],  # 网络类型
                    'country': '',  # 国家
                    'province': '',  # 省市
                    'operator': '',  # 运营商
                    'resp_speed': il.xpath('.//td[6]/text()')[0],  # 响应速度
                    'final_verify_time': il.xpath('.//td[7]/text()')[0],  # 最后验证时间
                    'life': '',  # 存活时间
                    'num': 3
                }

    @classmethod
    def freeProxyEight(cls, page_count=2):
        for i in range(1, page_count + 1):
            url = 'http://ip.jiangxianli.com/?page={}'.format(i)
            html_tree = getHtmlTree(url)
            # tr_list = html_tree.xpath("/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr")
            tr_list = html_tree.xpath('.//table/tbody/tr')
            if len(tr_list) == 0:
                continue
            for il in tr_list:
                # yield tr.xpath("./td[2]/text()")[0] + ":" + tr.xpath("./td[3]/text()")[0]
                # o(il.xpath('.//td[6]/text()')[0] if len(il.xpath('.//td[6]/text()')) != 0 else '333')
                yield {
                    'ip': il.xpath('.//td[2]/text()')[0],  # 地址
                    'port': il.xpath('.//td[3]/text()')[0],  # 端口
                    'anonymity': il.xpath('.//td[4]/text()')[0],  # 透明度
                    'type': il.xpath('.//td[5]/text()')[0],  # 网络类型
                    'country': '',  # 国家
                    'province': il.xpath('.//td[6]/text()')[0] if len(il.xpath('.//td[6]/text()')) != 0 else '',  # 省市
                    'operator': il.xpath('.//td[7]/text()')[0] if len(il.xpath('.//td[7]/text()')) != 0 else '',  # 运营商
                    'resp_speed': il.xpath('.//td[8]/text()')[0],  # 响应速度
                    'final_verify_time': il.xpath('.//td[9]/text()')[0],  # 最后验证时间
                    'life': '',  # 存活时间
                    'num': 3
                }

    @classmethod
    def freeProxyNinth(cls):
        urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1']
        request = WebRequest()
        for url in urls:
            r = request.get(url, timeout=30)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield {
                    'ip': proxy[0],  # 地址
                    'port': proxy[1],  # 端口
                    'anonymity': '',  # 透明度
                    'type': '',  # 网络类型
                    'country': '',  # 国家
                    'province': '',  # 省市
                    'operator': '',  # 运营商
                    'resp_speed': '',  # 响应速度
                    'final_verify_time': '',  # 最后验证时间
                    'life': '',  # 存活时间
                    'num': 3
                }

    @staticmethod
    def driver(url, headers, cookie=None):
        # print(url)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('user-agent=' + headers['User-Agent'])
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        if cookie is not None:
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
    d = g.freeProxyFirst()
    # d = g.freeProxySecond()
    # d = g.freeProxyThird()
    # d = g.freeProxyFourth()
    # d = g.freeProxyFifth()
    # d = g.freeProxySixth()
    # d = g.freeProxySeventh()
    # d = g.freeProxyEight()
    # d = g.freeProxyNinth()
    # for i in d:
    #     o(i)
    from ProxyGetter.CheckProxy import CheckProxy

    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxyFirst)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxySecond)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxyThird)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxyFourth)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxyFifth)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxySixth)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxySeventh)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxyEight)
    CheckProxy.checkGetProxyFunc(GetFreeProxy.freeProxyNinth)
