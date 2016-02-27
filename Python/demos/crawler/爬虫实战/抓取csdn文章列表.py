# -*- coding: utf-8 -*-

from urllib import request
import re

#访问不存在的页数时会列出所有文章列表
url = 'http://write.blog.csdn.net/postlist/0/0/enabled/100'
req = request.Request(url)

#没有User-agent信息会禁止访问
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36\
    QQBrowser/9.3.6581.400')

#不加cookie信息就没有登录信息，就会读取不到
req.add_header('Cookie', 'uuid_tt_dd=-4456677632578794343_20151102;\
    __gads=ID=f5f418612f6b6851:T=1446469919:S=ALNI_MYQPZGdMxcmo8mzOP9r_gOdrxJ7Vw;\
    __qca=P0-15466875-1446469925056; \
    CloudGuest=WxgavMeFZUnIeAvrTXPr2HfdEJQ3XNI/ogkWMXEYElrjN9NlbAWbS3eWZ7xSzLptZLM/\
    IAP5Ggvc98x/jYhoxWEYLCEYayWsY7r8fuf7UVENR4egptFlIbwReWpYmUiiu9eL8HINRfmwSoJ2nxq4oEgVvq/\
    iODtrr96jQRTAXRocuSja/6aqx8ObeeFz13T2; \
    postedit_code=java; lzstat_uv=24863415231519359084|3578454@2997217; \
    __message_district_code=350000; _ga=GA1.2.40350255.1446469921; _gat=1; \
    UserName=passion_wu128; UserInfo=Zz8rb7pzHk5msh8aYLrIhjnHkPeetTq52JtDHpCMaoQIpCHQny3bG7K20YUyFQQAF5NLfWaO0ZgIgfqDyIn%2FpxTB%2BW6D9YTrs9mUtp5chplcT%2BUc7rcENrvd2yItJx3hRD0uZhMpQ75R8EeKXv3%2B3Q%3D%3D; \
    UserNick=passion_wu128; AU=6B9; UN=passion_wu128; UE="passion_wu@126.com"; \
    access-token=0768f603-5c38-4cea-9e31-6d45ecc22fb9; dc_tos=o2inch; \
    __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; \
    __message_in_school=0; dc_session_id=1455417517699')

with request.urlopen(req) as req:
    content = req.read().decode('utf-8', errors='ignore')
    #content = "<td class='tdleft'><a href='http://blog.csdn.net/passion_wu128/article/details/50103513' target=_blank>hibernate入门实例</a><span class='gray'>（2015-11-30 00:42）</span></td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>"
    #*后面加？是采用非贪婪模式，及遇到第一个</td>就结束，而贪婪模式会遇到最后一个</td>才结束
    pattern = re.compile("<td class='tdleft'><a.*?>(.*?)</a>.*?</td>")
    #print(content)
    items = pattern.findall(content)
    for index, item in enumerate(items):
        print('{},{}'.format(index+1, item))