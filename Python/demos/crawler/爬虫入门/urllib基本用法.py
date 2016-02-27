# -*- coding: utf-8 -*-

from urllib import request

url = 'http://www.baidi.com'

#request.urlopen returns a http.client.HTTPResponse object
if 0:
    with request.urlopen(url) as f:
        print('version:', f.version) #10 for HTTP/1.0, 11 for HTTP/1.1.
        print('status:', f.status)   #200 is OK
        print('reason:', f.reason)
        print('header:')
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('data:', f.read().decode('utf-8'))

    print('Data:', f.read().decode('utf-8'))
# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
    'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('version:', f.version) #10 for HTTP/1.0, 11 for HTTP/1.1.
    print('status:', f.status)   #200 is OK
    print('reason:', f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))