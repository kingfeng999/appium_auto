#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 1:38
# @Author  : qinzhifeng
# @FileName: shoushijiesuo.py
# @Software: PyCharm

''' 手机图案解锁案例 '''

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# 配置项
desired_cap = dict()
desired_cap["platformName"] = "Android"
desired_cap["platformVersion"] = "5.1.1"
desired_cap["deviceName"] = "10.0.0.1:5555"
desired_cap['appPackage'] = 'com.android.settings'   # 夜神模拟器的包名
desired_cap['appActivity'] = '.Settings'             # 夜神模拟器的设置页面
desired_cap["noSign"] = True                # 不重新签名
desired_cap['unicodeKeyboard'] = True       # 使用 Unicode input 输入法,支持中文输入并隐藏键盘，默认是 false
desired_cap['resetKeyboard'] = True         # 在运行了 unicodeKeyboard 完成测试后将输入法重置为原有状态，如果单独使用该参数将被忽略，默认值是 false
desired_cap['autoGrantPermisions'] = True   # 自动同意 app 所需要的各项权限，默认是 false

# 构造 driver   webdriver
# http://localhost:4723/wd/hub   appium 的地址
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)

'''
TouchAction 可以实现⼀些针对⼿势的操作，⽐如滑动、⻓按、拖动等。我们 可以将这些基本⼿势组合 成⼀个相对复杂的⼿势。
⽐如，我们解锁⼿机或者⼀些应⽤软件都有⼿势解 锁的这种⽅式。 
使⽤步骤 
1. 创建 TouchAction 对象 
2. 通过对象调⽤想执⾏的⼿势 
3. 通过 perform() 执⾏动作 
方法：TouchAction(driver).press(x=120,y=420).wait(10).move_to(x=120, y=660).release().perform()
'''

TouchAction(driver).press(x=319,y=1282).wait(10).move_to(x=319,y=1497).\
    move_to(x=319,y=1713).move_to(x=532,y=1713).move_to(x=760,y=1713).release().perform()