# -*- coding: utf-8 -*-

from urllib import request
import re
import xlwt

# date_begin = input('要查询的开始日期(例如:2013-01-01):')
# date_end = input('要查询的结束日期(例如:2016-02-14):')
date_begin = '2015-01-01'
date_end = '2016-01-01'
url = 'http://baidu.lecai.com/lottery/draw/list/50?type=range_date&start={}&end={}'.format(
        date_begin, date_end)
req = request.Request(url)

#没有User-agent信息会禁止访问
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36\
    QQBrowser/9.3.6581.400')

with request.urlopen(req) as req:
    content = req.read().decode('utf-8', errors='ignore')
    # 匹配每一个开奖日的数据
    # .*后面加问号表示非贪婪匹配
    # re.S表示.*可以匹配换行符
    pattern_row = re.compile('<td><a href=.*?>(.*?)</a></td>[\s]*'
                         '<td>(.*?)</td>.*?'
                         '<td class="redBalls">(.*?)</td>.*?'
                         '<td class="blueBalls">(.*?)</td>.*?'
                         '<td class="NotNumber">([\d]+)</td>.*?'
                         '<td class="cash">([\d]+)</td>.*?'
                         '<td class="NotNumber">([\d]+)</td>.*?'
                         '<td class="cash">([\d]+)</td>.*?'
                         ,re.S)
    #匹配开奖号码
    pattern_ball = re.compile('<em>(.*?)</em>')
    items = pattern_row.findall(content)
    file = xlwt.Workbook()
    table = file.add_sheet('历史数据', cell_overwrite_ok=True)
    head = ['期号', '开奖日期', '开奖号码', '一等奖注数', '一等奖金额', '二等奖注数', '二等奖金额']
    for index, value in enumerate(head):
        table.write(0, index, value)
    #按格式输出开奖结果并导出
    for index, item in enumerate(items):
        #提取红球号码
        ball_red = pattern_ball.findall(item[2])
        #提取篮球号码
        ball_blue = pattern_ball.findall(item[3])
        ball_str = '[{} {} {} {} {} {}-{}'.format(ball_red[0], ball_red[1], ball_red[2],
                                    ball_red[3], ball_red[4], ball_red[5],ball_blue[0])
        #篮球号码可能有两个
        if len(ball_blue)==2:
            ball_str = ball_str + ' {}'.format(ball_red[1])
        ball_str = ball_str + ']'
        print('{:<4} {:<10}{:<12}\t{:<28}{:<6}{:<10}\t{:<6}\t{}'.format(index+1, item[0], item[1],
               ball_str, item[4], item[5], item[6], item[7]))
        #导出到excel文件
        table.write(index+1, 0, item[0])
        table.write(index+1, 1, item[1])
        table.write(index+1, 2, ball_str)
        table.write(index+1, 3, item[4])
        table.write(index+1, 4, item[5])
        table.write(index+1, 5, item[6])
        table.write(index+1, 6, item[7])

    file.save('双色球开奖号码.xls')
