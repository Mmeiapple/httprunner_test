
import time
import random

now = time.strftime('%Y')
#1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
print(now)
second = random.randint(1948,int(now))
print(second)
age = int(now) - second
print('随机生成的身份证人员年龄为：'+str(age))
