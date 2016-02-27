# -*- coding: utf-8 -*-

import urllib
from urllib import request

def test_httperror():
    try:
        f = request.urlopen('http://blog.csdn.net/cqcre')
        print('version:', f.version) #10 for HTTP/1.0, 11 for HTTP/1.1.
        print('status:', f.status)   #200 is OK
        print('reason:', f.reason)
        print('header:')
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
    except urllib.error.HTTPError as e:
        print('code:', e.code)
        print(e.reason)
    except urllib.error.URLError as e:
        print(e.reason)
    except:
        print('Unknown error')

def main():
    test_httperror()

if __name__=='__main__':
    main()

