#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-31 19:14
# @Author  : qinzhifeng
# @FileName: settind_swipe.py
# @Software: PyCharm

from appium import webdriver
import time
from selenium.webdriver.common.by import By
from base_swipe import Swipe

# 配置项，第一种写法
desired_caps = {
  "platformName": "Android",                    # 定义平台类型：android/ios
  "platformVersion": "5.1.1",                   # 定义平台版本
  "deviceName": "10.0.0.1:5555",                # 定义设备名称：随便写不影响程序运行
  "appPackage": "com.douban.frodo",             # 定义程序包名
  "appActivity": ".activity.SplashActivity"     # 定义 activity 界面
}

# 配置项，第二种写法，通过 apk 安装的方式
desired_cap = dict()
desired_cap["platformName"] = "Android"
desired_cap["platformVersion"] = "5.1.1"
desired_cap["deviceName"] = "10.0.0.1:5555"
'''
1、通过安装 app 来直接驱动 app 的时候，需要配套加一个 noSign 参数，默认是 false 需要重新签名
2、所以需要敲定 noSign 的值为：True
原因：
防止 appium 对 app 重新签名，损坏 apk 的包，不能正常使用
'''
# desired_cap["app"] = r"C:\Users\P\Desktop\com.douban.frodo_6.36.0_186.apk"   # r进行转义
# desired_cap["udid"] = '127.0.0.1:62001'     # 定义运行的设备，如果存在多个设备则可以使用
desired_cap['appPackage'] = 'com.android.settings'   # 夜神模拟器的包名
desired_cap['appActivity'] = '.Settings'             # 夜神模拟器的设置页面
desired_cap["noSign"] = True                # 不重新签名
desired_cap['unicodeKeyboard'] = True       # 使用 Unicode input 输入法,支持中文输入并隐藏键盘，默认是 false
desired_cap['resetKeyboard'] = True         # 在运行了 unicodeKeyboard 完成测试后将输入法重置为原有状态，如果单独使用该参数将被忽略，默认值是 false
desired_cap['autoGrantPermisions'] = True   # 自动同意 app 所需要的各项权限，默认是 false

# 构造 driver   webdriver
# http://localhost:4723/wd/hub   appium 的地址
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
# 设置隐式等待，全局生效
driver.implicitly_wait(10)
time.sleep(10)      # 设置强制等待

# 夜神模拟器设置页面的滑动操作
swipe = Swipe(driver)
swipe.swipe_page(dir='down')
loc = By.XPATH,"//*[@text='关于平板电脑']"
el = Swipe(driver).find_element_with_scroll(loc)
el.click()

# 元素定位
# el1 = driver.find_element_by_id("com.douban.frodo:id/entire_password_login")
# el1.click()
# el2 = driver.find_element_by_id("com.douban.frodo:id/input_user_name")
# el2.click()
# el2.send_keys("17610873228")
# el3 = driver.find_element_by_id("com.douban.frodo:id/input_password")
# el3.click()
# el3.send_keys("yaoyao123456")
# el4 = driver.find_element_by_id("com.douban.frodo:id/sign_in_douban")
# el4.click()

# xpath 定位
# driver.find_element_by_xpath("//*[@text='帐号密码登录']").click()

# 获取分辨率/窗口的大小
# print(driver.get_window_size())





