#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-28 18:31
# @Author  : qinzhifeng
# @FileName: h5_chrome.py
# @Software: PyCharm
'''
h5 页面自动化，需要连接真机
1、连接手机成功后，定位方式需要在电脑浏览器输入：chrome://inspect/#devices，自动获取 chrome 版本信息
2、需要获取手机对应的 chromedriver 版本，这里版本是 81
'''
import time

from appium import webdriver

# 启动配置项
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = '111111'
desired_caps['udid'] = '127.0.0.1:62001'

# 添加手机里面 chrome 浏览器所对应的 chromedriver 的绝对路径
desired_caps['chromedriverExecutable'] = r'C:\Users\P\PycharmProjects\appium\chromedriver_81\chromedriver.exe'
# 添加浏览器的名字
desired_caps['browserName'] = 'Chrome'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 接下来的操作跟 webui 自动化是一样的，定位元素的方式也是一样的
driver.get('http://121.42.15.146:9090/mtx/')
time.sleep(3)

# 定位到“我的”按钮，如下 xpath 是 android 的写法
driver.find_element_by_xpath('(//*[text()="我的"])[2]').click()
time.sleep(5)
driver.quit()   # 退出


