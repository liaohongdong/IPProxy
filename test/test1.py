import pprint

if __name__ == '__main__':
    b = bytes('string', encoding='utf-8')
    print(b)

    b = b.decode('utf-8')
    print(b)

    b = b.encode('utf-8')
    print(b)
