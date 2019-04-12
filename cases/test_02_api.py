import requests
import unittest
from utils import pyxlrd
loginName=pyxlrd.readxls("data1.xls","Sheet1",0,0)
telephone=int(pyxlrd.readxls("data1.xls","Sheet1",1,0))
email=pyxlrd.readxls("data1.xls","Sheet1",2,0)
loginPassword=pyxlrd.readxls("data1.xls","Sheet1",3,0)
userName=pyxlrd.readxls("data1.xls","Sheet1",5,0)
userIdentity=pyxlrd.readxls("data1.xls","Sheet1",6,0)
print(loginName,telephone,email,loginPassword,userName,userIdentity)
class TestApi(unittest.TestCase):
    '''
    接口测试
    '''
    def test_01_userSignin(self):
        '''
        注册接口
        '''
        url = "http://localhost:8080/morning/user/userSignin"
        payload = "user.loginName=%s&user.telephone=%s&user.email=%s&user.loginPassword=%s&registerCode=123456"%(loginName,telephone,email,loginPassword)
        headers = {
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        res = response.json()
        success = res["success"]
        self.assertEqual(True,success,"判断注册是否成功")


    def test_02_sendEmail(self):
        '''
        验证码接口
        '''
        url = "http://localhost:8080/morning/sendEmail"
        payload = "email=%s&type=0"% email
        headers = {
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        res = response.json()
        global entity
        entity = res["entity"]
        success = res["success"]
        self.assertEqual(True,success,"判断发送验证码是否成功")

