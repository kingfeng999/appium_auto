#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 23:41
# @Author  : qinzhifeng
# @FileName: douban_login_inspect_findApi.py
# @Software: PyCharm

import time
from appium import webdriver
from base_swipe import Swipe
# 配置项，第一种写法
desired_caps = {
    "platformName": "Android",  # 定义平台类型：android/ios
    "platformVersion": "5.1.1",  # 定义平台版本
    "deviceName": "10.0.0.1:5555",  # 定义设备名称：随便写不影响程序运行
    "appPackage": "com.douban.frodo",  # 定义程序包名
    "appActivity": ".activity.SplashActivity",  # 定义 activity 界面
    "noSign": True,  # 不需要 app 重新签名
    "unicodeKeyboard": True,  # 使用 Unicode input 输入法,支持中文输入并隐藏键盘，默认是 false
    "resetKeyboard": True,  # 在运行了 unicodeKeyboard 完成测试后将输入法重置为原有状态，如果单独使用该参数将被忽略，默认值是 false
    "autoGrantPermisions": True  # 自动同意 app 所需要的各项权限，默认是 false
}

# 创建 driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@text="帐号密码登录"]').click()
# 输入手机号码
driver.find_element_by_xpath('//*[@text="请输入手机号/邮箱"]').send_keys('13802282483')
# 输入手机密码
driver.find_element_by_id('com.douban.frodo:id/input_password').send_keys('1972f73x')
# 点击登录按钮
driver.find_element_by_xpath('//*[@text="登录"]').click()
# 点击我的
driver.find_element_by_xpath('//*[@text="我的"]').click()
# 点击个人主页
driver.find_element_by_xpath('//*[@text="个人主页"]').click()
# 点击编辑个人资料
driver.find_element_by_xpath('//*[@text="编辑个人资料"]').click()
# 选择性别
driver.find_element_by_id('com.douban.frodo:id/male').click()
# 输入个人简介
jianjie = driver.find_element_by_xpath('//*[@text="输入简介（选填）"]')
jianjie.clear()
jianjie.send_keys('这是我的个人简介，希望你喜欢！')
# 选择城市 == 北京
driver.find_element_by_id('com.douban.frodo:id/select_city_action').click()
driver.find_element_by_xpath('//*[@text="北京"]').click()
# 选择生日
driver.find_element_by_id('com.douban.frodo:id/birthday').click()
time.sleep(2)

# 调用Swipe类，并且要传定位的元素、滑动次数、滑动方向等
# 滑动年、月、日
year = driver.find_elements_by_id('android:id/numberpicker_input')[0]
Swipe(driver).el_swipe(year, 3, 'up')
month = driver.find_elements_by_id('android:id/numberpicker_input')[1]
Swipe(driver).el_swipe(month, 3, 'up')
day = driver.find_elements_by_id('android:id/numberpicker_input')[2]
Swipe(driver).el_swipe(day, 3, 'up')

driver.find_element_by_xpath('//*[@text="确定"]')
driver.find_element_by_xpath('//*[@text="保存"]')
driver.find_element_by_xpath('//*[@text="我知道了"]')
