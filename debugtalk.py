
import requests
import re
import json
import random



def get_token(appid,secret,url="https://api.weixin.qq.com/"):
    data={'grant_type':'client_credential','appid':appid,'secret':secret}
    response=requests.get(url=url+'cgi-bin/token?',params=data)
    text=response.content.decode('utf-8')
    token=re.findall('"access_token":"(.+?)"',text)[0]
    return token


def creat_phone_move(count):#生成移动手机号
    phone=[]
    for i in range(count):
        # 第二位数
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数
        third = {
            3: [4,5,6,7,8][random.randint(0,4)],
            4: [7][0],
            5: [0,1,2,4,7,8,9][random.randint(0,6)],
            7: [8][0],
            8: [2,3,4,7,8][random.randint(0,4)]
        }[second]
        # 后八位数
        suffix = ''
        for j in range(0, 8):
            suffix = suffix + str(random.randint(0, 9))

        phone.append("1{}{}{}".format(second, third, suffix))
    return phone

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
    token=get_token("wx60536c088aee3040","f214d833f873d8cc1b38255eca0938d9")
    print(token)
    print(setup_case("ces01"))
    print(teardown_case("ces01"))
    print(setup_step("ces01"))
    print(teardown_step("ces01"))
    phone=creat_phone_move(2)
    print(phone)
