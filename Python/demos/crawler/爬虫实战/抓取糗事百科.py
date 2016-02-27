# -*- coding: utf-8 -*-

from urllib import request
import re

total = int(input('input the number you want to crawler:'))
current = 0
page_number = 0
while True:
    page_number += 1
    req = request.Request('http://www.qiushibaike.com/hot/page/{}'.format(page_number))
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
        'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        content = f.read().decode('utf-8', errors='ignore')
        #print(content)
        #</div>后面跟的是<!则表示该内容没有图片
        pattern = re.compile('<div class="fs-l mlr mt10">[\s]*(.*)[\s]*</div>[\s]*<!')
        items = pattern.findall(content)
        for item in items:
            print('{},{}\n'.format(current+1, item))
            current += 1
            if current == total:
                break
    if current == total:
        break