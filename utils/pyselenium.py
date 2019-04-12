from selenium import webdriver
from config import chromepath

class PySelenium():
    def __init__(self,drivername="Chrome"):
        if drivername == "Chrome":
            driver = webdriver.Chrome(executable_path=chromepath)
        elif drivername == "IE":
            driver = webdriver.Ie(executable_path="")
        elif drivername == "Safari":
            driver = webdriver.Safari(executable_path="")
        elif drivername == "Edge":
            driver = webdriver.Edge(executable_path="")
        elif drivername == "Firefox":
            driver = webdriver.Firefox(executable_path="")
        else:
            print("请选择正确的浏览器！！！")
            raise
        self.driver = driver

    def get_element(self,byvalue):
        '''
        获取元素对象
        '''
        bvlist = byvalue.split("->")
        by = bvlist[0]
        value = bvlist[1]
        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by=='name':
            element=self.driver.find_element_by_name(value)
        elif by=='xpath':
            element=self.driver.find_element_by_xpath(value)
        elif by=='tag':
            element=self.driver.find_elements_by_tag_name(value)
        elif by=='class':
            element=self.driver.find_element_by_class_name(value)
        elif by=='link':
            element=self.driver.find_element_by_link_text(value)
        elif by=='partial':
            element=self.driver.find_element_by_partial_link_text(value)
        elif by=='css':
            element=self.driver.find_element_by_css_selector(value)
        else:
            print("请选择正确的定位方式")
            raise
        return element
    
    def send(self,byvalue,value):
        element = self.get_element(byvalue)
        element.send_keys(value)

    def open_url(self,url):
        '''
        打开网页
        '''
        self.driver.get(url)

    def click(self,byvalue):
        '''
        点击
        '''
        element = self.get_element(byvalue)
        element.click()
    
    def get_title(self):
        return self.driver.title

    def quit(self):
        self.driver.quit()

