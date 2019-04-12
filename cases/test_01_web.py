import unittest
# from selenium import webdriver
from utils import pyselenium
import time
class TestWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始测试。。。。。")
        cls.driver=pyselenium.PySelenium()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("\n测试结束。。。。。")
    def test_01(self):    
        driver=self.driver
        driver.open_url("http://www.baidu.com")
        driver.send('id->kw','iphone')
        time.sleep(2)
        driver.click('id->su')
        time.sleep(2)
        title=driver.get_title()
        self.assertIn("iphone",title)
    def test_02(self):    
        driver=self.driver
        driver.open_url("http://www.baidu.com")
        driver.send('id->kw','小米')
        time.sleep(2)
        driver.click('id->su')
        time.sleep(2)
        title=driver.get_title()
        self.assertIn("小米",title)
    def test_03(self):    
        driver=self.driver
        driver.open_url("http://www.baidu.com")
        driver.send('id->kw','华为')
        time.sleep(2)
        driver.click('id->su')
        time.sleep(2)
        title=driver.get_title()
        self.assertIn("华为",title)

