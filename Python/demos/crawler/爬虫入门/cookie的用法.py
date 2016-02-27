import http.cookiejar, urllib.request
from urllib import request

def save_cookie():
    cj = http.cookiejar.MozillaCookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open("http://www.baidu.com")
    for item in cj:
        print('{}->{}'.format(item.name, item.value))
    cj.save("cookie.txt")

def load_cookie():
    cj = http.cookiejar.MozillaCookieJar()
    cj.load('cookie.txt')
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open("http://www.baidu.com")
    for item in cj:
        print('{}->{}'.format(item.name, item.value))

# save_cookie()
load_cookie()
