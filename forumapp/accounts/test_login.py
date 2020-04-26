from django.test import TestCase
from selenium import webdriver
from time import sleep
import unittest

# 创建TestBaidu类，继承unittest.TestCase;实现定位搜索，验证搜索，定位打开新页面
class TestLogin(unittest.TestCase):
    # 用例执行前准备工作
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 在TestBaidu类下构造test_baidu()方法
    def test_wrong_username(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        sleep(5)
        
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("mikot")

        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("hellohcn")
        driver.find_element_by_id("login_submit").click() # 定位搜索

        self.assertIn("127.0.0.1:8000/accounts/login/", self.driver.current_url)
        sleep(5)

    def test_true(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        sleep(5)
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("mikoto")

        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("hellohcn")
        driver.find_element_by_id("login_submit").click() # 定位搜索

        self.assertIn("http://127.0.0.1:8000/test/", self.driver.current_url)
        sleep(5)

    def test_wrong_password(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        sleep(5)
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("mikoto")

        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("hellohcn0")
        driver.find_element_by_id("login_submit").click() # 定位搜索

        self.assertIn("http://127.0.0.1:8000/accounts/login/", self.driver.current_url)
        sleep(5)

    def test_both_wrong(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        sleep(5)
        driver.find_element_by_id("id_username").send_keys("mikot")

        driver.find_element_by_id("id_password").send_keys("hellohc")
        driver.find_element_by_id("login_submit").click() # 定位搜索

        self.assertIn("http://127.0.0.1:8000/accounts/login/", self.driver.current_url)
        sleep(5)

    def test_no_username(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        sleep(5)

        driver.find_element_by_id("id_password").send_keys("hellohcn")
        driver.find_element_by_id("login_submit").click() # 定位搜索

        self.assertIn("http://127.0.0.1:8000/accounts/login/", self.driver.current_url)

        sleep(3)
    # 用例执行后的处理操作
    def tearDown(self):
        self.driver.quit()

# 调试TestBaidu测试类
if __name__ == '__main__':
    unittest.main()
# Create your tests here.
