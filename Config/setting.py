DATABASES = {
    "default": {
        "TYPE": "redis",
        "HOST": "39.108.115.177",
        "PORT": 6379,
        "NAME": "proxy",
        "PASSWORD": ""
    }
}

PROXY_GETTER = [
    "freeProxyFirst",
    "freeProxySecond",
    # "freeProxyThird",  # 网站已不能访问
    "freeProxyFourth",
    "freeProxyFifth",
    # "freeProxySixth"   # 不再提供免费代理
    "freeProxySeventh",
    # "freeProxyEight",
    # "freeProxyNinth",
    "freeProxyTen",
    "freeProxyEleven",
    "freeProxyTwelve",
    # foreign website, outside the wall
    # "freeProxyWallFirst",
    # "freeProxyWallSecond",
    # "freeProxyWallThird"
]

SERVER_API = {
    "HOST": "0.0.0.0",
    "PORT": 5000
}

if __name__ == '__main__':
    data = DATABASES
    d = data.get("default", {}).get("TYPE", "")
    print(d)
