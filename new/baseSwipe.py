#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-28 17:32
# @Author  : qinzhifeng
# @FileName: baseSwipe.py
# @Software: PyCharm

import time

class Swipe(object):
    def __init__(self, driver):
        self.driver = driver

    # 封装上下滑动操作（针对目标值滑动的操作）
    def swipe_el_destination(self, el, destination):
        '''
        el是定位到的元素，调用时如果定位是年就传年，月就传月，日就传日，destination是目标值，要滑动到的具体数值
        '''
        # 元素的位置,x,y
        el_size = el.size
        el_width = el_size['width']
        el_height = el_size['height']
        # 排查错误的方式
        print(f'进入代码获取的el_width是{el_width}，el_height是{el_height}')
        # 获取元素的x,y坐标
        el_location = el.location
        el_x = el_location['x']
        el_y = el_location['y']
        print(f'进入代码获取的el_x是{el_x}，el_y是{el_y}')
        swipe_x = int((el_x + el_width) * 0.9)
        swipe_y2 = int((el_y + el_height))
        # 获取当前元素的text的值，因为text属性就是年的具体值，月的具体值，日的具体值
        while True:
            # time.sleep(5)s
            # 可以获取到当前页面元素的值
            now = el.text
            # time.sleep(5)
            print('now 是多少', now)
            # time.sleep(5)
            if now > destination:
                print('now>的值是多少',now)
                time.sleep(3)
                # 向下滑动，y值变大
                print(swipe_x)
                print(el_y)
                print(swipe_y2)
                print('+++++++++++++')
                self.driver.swipe(swipe_x,el_y,swipe_x,swipe_y2,duration=1000)
                print('向下滑动')
                # time.sleep(3)
            elif now < destination:
                print('now<的值是多少', now)
                # 向上滑动，y值变小
                self.driver.swipe(swipe_x, swipe_y2, swipe_x, el_y,duration=1000)
                print('向上滑动')
                # time.sleep(3)
            elif now == destination:
                print('now==的值是多少', now)
                print('数值调整完成')
                break

    def el_swipe(self, el, n, flag):
        '''
        size返回的是宽高，location返回的是x,y坐标位置
        :param el: 在el元素这个范围进行滑动
        :param n: 滑动的次数
        :param flag: 滑动的方向 1:swipe_up,-1:swipe_down
        :return:
        '''
        # 获取元素的宽高
        el_size = el.size
        el_width = el_size['width']
        el_height = el_size['height']
        # 获取元素的x,y坐标
        el_location = el.location
        el_x = el_location['x']
        el_y = el_location['y']
        swipe_x1 = int((el_x + el_width) * 0.9)
        swipe_y1 = el_y
        swipe_y2 = int((el_y + el_height) * 0.9)
        if flag == -1:
            print('{}元素开始向下滑动'.format(el))
            for i in range(n):
                self.driver.swipe(swipe_x1, swipe_y1, swipe_x1, swipe_y2, 3500)
                time.sleep(1)
        else:
            print('{}元素开始向上滑动'.format(el))
            for i in range(n):
                self.driver.swipe(swipe_x1, swipe_y2, swipe_x1, swipe_y1, 3500)
                time.sleep(1)


    def scroll_page_one_time(self, dir="up", duration=3000):
        """
        滑动一次屏幕
        :param dir: 滑动的方向
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return:
        """
        # 滑动
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        top_x = screen_width * 0.5
        top_y = screen_height * 0.25
        bottom_x = screen_width * 0.5
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = screen_height * 0.5
        right_x = screen_width * 0.75
        right_y = screen_height * 0.5

        # 根据方向参数，去滑动
        if dir == "up":
            time.sleep(1)
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, duration)
        elif dir == "down":
            time.sleep(1)
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, duration)
        elif dir == "left":
            time.sleep(1)
            self.driver.swipe(right_x, right_y, left_x, left_y, duration)
        elif dir == "right":
            time.sleep(1)
            self.driver.swipe(left_x, left_y, right_x, right_y, duration)
        else:
            raise Exception("请输入正确的滑动方向 up/down/left/right")

    def find_element_with_scroll(self, feature, dir="up"):
        """
        # 边滑动边找元素
        按照 dir 的方向滑动，并且找到 feature 这个特征的元素
        :param dir:
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return: 找到的元素
        """
        while True:
            try:
                # 如果找到关于手机，就段点进去
                # driver.find_element_by_xpath("//*[@text='用户']").click()
                return self.driver.find_element(*feature)
            except:
                # 记录一下滑动之前的page_source
                old_page_source = self.driver.page_source

                self.scroll_page_one_time(dir)

                # 判断滑动之后是不是和之前的页面一样
                if old_page_source == self.driver.page_source:
                    raise Exception("到底了！请检查传入的元素的特征")

