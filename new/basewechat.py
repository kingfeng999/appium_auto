#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-28 22:13
# @Author  : qinzhifeng
# @FileName: basewechat.py
# @Software: PyCharm

'''
操作微信公众号
案例：爱心筹（混合app）
需要另外在工程目录下创建微信内核版本对应的 chromedriver ，这里版本是：77
'''

import time
from appium import webdriver

# 启动配置项qa
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = '111111'
desired_caps['udid'] = '127.0.0.1:62001'     # 设置手机设备ID

# 添加手机里面 chrome 浏览器所对应的 chromedriver 的绝对路径
# 使用场景：
# 1、需要在浏览器里面打开页面的时候
# 2、app 混合（app 原生 + h5页面）
desired_caps['chromedriverExecutable'] = r'C:\Users\P\PycharmProjects\appium\chromedriver_77.0.3865.10\chromedriver.exe'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'

# 微信公众号要加上这个参数，是固定的
desired_caps['chromeOptions'] = {
    'androidProcess' : 'com.tencent.mm:tools'
}

desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 不重新设置应用，以下必须设置，否则会清空，默认不清空
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 进入微信操作，如下 xpath 属于 web 的写法
driver.find_element_by_xpath('//*[@text="通讯录"]').click()
driver.find_element_by_xpath('//*[@text="公众号"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@text="爱心筹"]').click()
driver.find_element_by_xpath('//*[@text="我的筹款"]').click()
driver.find_element_by_xpath('//*[contains(@text,"我要提现")]').click()
time.sleep(4)

# 打印当前页面所有的 webview，如果 webview 页面比较多，则需要一个一个去切换确定
cts = driver.contexts
# todo 打印的内容如果包含了 WEBVIEW_com 就是 h5 页面，包含 NATIVE_APP 是原生页面
# todo 打印出两个内容: 'WEBVIEW_com.tencent.mm:tools'、'NATIVE_APP'
print(cts)
# 原则：
# 切换到 webview 页面（h5页面），之后的操作都是按照 webui 自动化去定位完成
# 如果又变成原生页面，那么需要切换回到 native（原生）页面
# todo 切换上下文：driver.switch_to.context()
time.sleep(5)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
driver.find_element_by_partial_link_text('提现').click()
time.sleep(5)
driver.find_element_by_partial_link_text('去添加').click()
time.sleep(5)
# todo 切换回原生页面，退出 driver
driver.switch_to.context('NATIVE_APP')
driver.quit()

