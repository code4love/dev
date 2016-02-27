# -*- coding: utf-8 -*-


# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str
# 请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    #先检查时区字符串是否符合规范
    tz_pattern = r'^UTC[+-]\d{1,2}:00'
    if re.match(tz_pattern, tz_str) is None:
        print('wrong argument:', tz_str)
        return 0
    colon_index = tz_str.index(':')
    tz_number = int(tz_str[3:colon_index])
    tz = timezone(timedelta(hours=tz_number))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    return dt.replace(tzinfo=tz).timestamp()

def main():
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0
    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0
    print('Pass')

if __name__ == '__main__':
    main()

