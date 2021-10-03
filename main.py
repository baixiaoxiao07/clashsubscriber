import os
import datetime
# 获取当前日期
print(datetime.date.today())
# 获取当前日期及时分秒
print(datetime.datetime.now())
# 获取当前时间写入文本中
with open('clash.yaml','w+')  as fp:
    fp.write(str(datetime.datetime.now()))
