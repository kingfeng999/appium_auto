#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-30 1:54
# @Author  : qinzhifeng
# @FileName: xiaochengxu.py
# @Software: PyCharm
'''
微信小程序自动化
案例：腾讯视频
1、混合  原生 app（定位方式：appium inspect/uiautomatorviewer）+ h5（定位方式：chrome://inspect/#devices）
'''

import time
from appium import webdriver

# 启动配置项qa
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'uiautomator1'   # automationName 安卓的引擎，把 h5 页面强转成原生 app 页面
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = '111111'
desired_caps['udid'] = '127.0.0.1:62001'     # 设置手机设备ID
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 不重新设置应用，以下必须设置，否则会清空，默认不清空
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_xpath('//*[@text="发现"]/..').click()  # 两个点，表示上一级
time.sleep(8)
driver.find_element_by_xpath('//*[@text="小程序"]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@text="腾讯课堂"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@text="搜索老师、机构、课程"]').send_keys('码同学')
time.sleep(6)
driver.find_element_by_xpath('//*[@text="【码同学】Python全栈自动化测试"]').click()
time.sleep(6)
driver.quit()