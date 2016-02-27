# -*- coding: utf-8 -*-

from urllib import request

url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"
with request.urlopen(url) as req:
    file = open('apic520.jpg', 'wb')
    file.write(req.read())
    file.close()