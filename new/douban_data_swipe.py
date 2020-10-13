#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-28 17:32
# @Author  : qinzhifeng
# @FileName: douban_data_swipe.py
# @Software: PyCharm

import time

from appium import webdriver

from new.baseSwipe import Swipe

# 启动配置项
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = '1111111'     # 随便写设备名称
desired_caps['udid'] = '127.0.0.1:62001'   # 指定设备 uid
desired_caps['appPackage'] = 'com.douban.frodo'
desired_caps['appActivity'] = 'com.douban.frodo.activity.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@text="帐号密码登录"]').click()
# driver.find_element_by_id('com.douban.frodo:id/entire_password_login_text').click()
# 用uiautomatorviewer去查看定位元素，发现这个textView一共有5个，帐户密码登录应该是第四个，
# 返回值是一个列表，然后索引值是3
# time.sleep(8)
# 如果不加time.sleep()的话，就会在刚进入页面的时候找到这个元素，然后停止查找，所以不建议用
# class_name()因为并没有什么用处，因为重复太多了，一点不准确
# el = driver.find_elements_by_class_name('android.widget.TextView')
# print(el)
driver.find_element_by_xpath('//*[@text="请输入手机号/邮箱"]').send_keys('13802282483')
driver.find_element_by_id('com.douban.frodo:id/input_password').send_keys('1972f73x')
driver.find_element_by_xpath('//*[@text="登录"]').click()
driver.find_element_by_xpath('//*[@text="我的"]').click()
driver.find_element_by_xpath('//*[@text="个人主页"]').click()
driver.find_element_by_xpath('//*[@text="编辑个人资料"]').click()
driver.find_element_by_xpath('//*[@text="选择生日（选填）"]').click()

# 调用时，传入定位到的元素并赋值给 now
now= driver.find_elements_by_id("android:id/numberpicker_input")[0]

# 1996 是目标值
Swipe(driver).swipe_el_destination(now, '1996')









