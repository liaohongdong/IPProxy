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
    # "freeProxySecond",
    # "freeProxyThird",
    # "freeProxyFourth",
    # "freeProxyFifth",
    # "freeProxySixth",
    # "freeProxySeventh",
    # "freeProxyEight",
    # "freeProxyNinth",
]

SERVER_API = {
    "HOST": "0.0.0.0",
    "PORT": 5000
}

if __name__ == '__main__':
    data = DATABASES
    d = data.get("default", {}).get("TYPE", "")
    print(d)
