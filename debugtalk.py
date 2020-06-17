
import requests
import re
import json
import time
import random



'''

获取token

'''

def get_token(appid,secret,url="https://api.weixin.qq.com/"):
    data={'grant_type':'client_credential','appid':appid,'secret':secret}
    response=requests.get(url=url+'cgi-bin/token?',params=data)
    text=response.content.decode('utf-8')
    token=re.findall('"access_token":"(.+?)"',text)[0]
    return token

'''
生成手机号码

'''

def creat_phone_move(count):#生成移动手机号
    phone=[]
    for i in range(count):
        ''' 第二位数'''
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        '''第三位数'''
        third = {
            3: [4,5,6,7,8][random.randint(0,4)],
            4: [7][0],
            5: [0,1,2,4,7,8,9][random.randint(0,6)],
            7: [8][0],
            8: [2,3,4,7,8][random.randint(0,4)]
        }[second]
        '''后八位'''
        suffix = ''
        for j in range(0, 8):
            suffix = suffix + str(random.randint(0, 9))

        phone.append("1{}{}{}".format(second, third, suffix))
    return phone


'''
生成身份证

'''

class GenerateIdCard():
    def __init__(self):
        pass
    def region(self):
        '''生成身份证前六位'''
        region_list=['362402','362421','362422','362423','362424','362425','362426','362427','431224']
        fist_list=random.choice(region_list)
        return fist_list

    def year(self):
        '''生成身份证年份'''
        now=time.strftime("%Y")
        second=random.randint(1948,int(now))
        return second

    def month(self):
        '''生成身份证月份'''
        three=random.randint(1,12)
        if three<10:
            return '0'+str(three)
        else:
            return three

    def day(self):
        '''生成身份证日期'''
        foud=random.randint(1,31)
        if foud <10:
            return '0'+str(foud)
        else:
            return foud
    def tail(self):
        five=random.randint(1,9999)
        if five<10:
            return '000'+str(five)
        if 10<five<100:
            return '00'+str(five)
        if 100<five<1000:
            return '0'+str(five)
        else:
            return five
    def generate_id_card(self):
        idCard=str(self.region())+str(self.year())+str(self.month())+str(self.day())+str(self.tail())
        return idCard

'''
创建身份证ID

'''

def creat_id(count):
    idCard=[]
    for i in range(count):
        id=GenerateIdCard().generate_id_card()
        idCard.append(id)
    return idCard




'''

生成随机字符串

'''
def random_string():
    list1=[]
    list=random.sample('sdhjkshfjkaasfafaf',5)
    string="".join(list)
    list1.append(string)
    return list1


def setup_case(casename):

    print("**************--------*********************")

    print('\n'+"测试用例: {} 开始".format(casename)+'\n')

def teardown_case(casename):

    print("**************--------*********************")


    print('\n'+"测试用例: {} 开始".format(casename)+'\n')

def setup_step(casename):

    print("**************--------*********************")


    print('\n'+"测试步骤: {} 开始".format(casename)+'\n')

def teardown_step(casename):

    print("**************--------*********************")


    print('\n'+"测骤: {} 结束".format(casename)+'\n')

if __name__=="__main__":
    print(random_string())
