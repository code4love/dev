# -*- coding: utf-8 -*-

# datetime是Python处理日期和时间的标准库。


#----------获取当前日期和时间----------
from datetime import datetime
now = datetime.now()
print(now)


#----------datetime转换为timestamp----------
dt = datetime(2015, 4, 19, 12, 20, 15, 123)
print(dt.timestamp())


#----------timestamp转换为datetime----------
#timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
#fromtimestamp将timestamp转换为本地时间
#utcfromtimestamp将timestamp转换为UTC标准时间
#北京时间是UTC+8,所以本地时间会快八个小时
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))


# ----------str转换为datetime----------
# 注意:转换后的datetime是没有时区信息的。
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


# ----------datetime转换为str-----------
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


#----------datetime加减----------
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


#----------本地时间转换为UTC时间-----------
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)


#datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。