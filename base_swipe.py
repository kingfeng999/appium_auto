#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-02 16:22
# @Author  : qinzhifeng
# @FileName: base_swipe.py
# @Software: PyCharm

'''
封装滑动操作：  上下滑动，左右滑动
向下滑动，x 不变，y 从小到大
向上滑动，x 不变，y 从大到小
向左滑动，y 不变，x 从大到小
向右滑动，y 不变，x 从小到大
'''
import time


class Swipe():

    def __init__(self, driver):
        self.driver = driver

    # 页面上下左右滑动封装
    def swipe_page(self, dir='up', duration=3000):
        '''
        duration 是滑动持续时间，默认是从下向上滑动
        :param dir:
        滑动的方向，
        'up'：从下向上滑动，
        'down'：从上向下滑动，
        'right'：从左往右滑动，
        'left'：从右往左滑动
        :return:
        '''
        # 获取屏幕的分辨率，返回值是：{'width':,'height':}
        screen = self.driver.get_window_size()
        screen_width = screen['width']  # 获取宽
        screen_height = screen['height']  # 获取高
        ''' 上下滑动x不变，公式： 距离底部的y + 距离顶部的y = 1 '''
        x = screen_width * 0.5  # 横坐标取屏幕宽度的一半
        top_y = screen_height * 0.25  # 距离顶部y的距离
        button_y = screen_height * 0.75  # 距离底部y的距离

        ''' 左右滑动y不变，公式： 距离左边的x + 距离右边的x = 1 '''
        y = screen_height * 0.5  # 纵坐标取屏幕高度的一半
        left_x = screen_width * 0.25  # 距离屏幕左边x轴的距离
        right_x = screen_width * 0.75  # 距离屏幕右边x轴的距离
        if dir == 'up':
            # 从下向上滑动
            self.driver.swipe(x, button_y, x, top_y, duration)
        elif dir == 'down':
            # 从上向下滑动
            self.driver.swipe(x, top_y, x, button_y, duration)
        elif dir == 'left':
            # 从右往左滑动
            self.driver.swipe(right_x, y, left_x, y, duration)
        elif dir == 'right':
            # 从左往右滑动
            self.driver.swipe(left_x, y, right_x, y, duration)
        else:
            # 如果不是上面定义的操作，则抛出异常
            raise Exception('请输入正确的滑动方向，比如 up/down/left/right')

    # 从下往上多个页面循环滑动封装
    def find_element_with_scroll(self, loc, dir='up'):
        '''
          # 定义边滑动边找元素的方法，默认提供 loc 定位方式，默认滑动方式为：up，即从下往上滑动
          # loc 定位元素的方式，By.XPATH,'//*[@text=""]'
          # 原则：循环滑动，找元素，代码需要做一下细节的逻辑判断
        :param loc:
        :param dir:
        :return:
        '''
        # 定义一个死循环
        while True:
            # 找元素,如果能找到就把元素返还，如果找不到就抛出错误提示
            try:
                return self.driver.find_element(*loc)
            except:
                old_page_source = self.driver.page_source  # todo 记录一下滑动之前的页面
                self.swipe_page(dir)  # 报错就要走 except，证明当前屏幕没有要找的元素，需要继续滑动
                '''
                # todo 万一滑到底部仍然找不到元素，那该怎么办？
                # 滑到底部特点：页面不再变化，y值不变
                '''
                if old_page_source == self.driver.page_source:  # 如果滑动之前的页面等于现在滑动现在的页面，证明滑动到底部了
                    raise Exception('滑到底部了，请检查传入元素的定位方式')

    # 选择个人出生年月的滑动封装：第一种写法
    def el_swipe(self, el, n, dir):
        '''
        滑动 - 坐标  动态滑动  通过元素的宽高 + 坐标值属性，动态获取
        :param el: 对哪个元素进行滑动操作
        :param n:  滑动的次数
        :param dir:  滑动的方向  up：向上滑动，down：向下滑动
        :return:
        '''
        # 向上或者向下滑动，x 轴不变
        # 通过元素的总 size，获取元素的宽和高，el_size返回的是字典
        el_size = el.size
        el_width = el_size['width']
        el_height = el_size['height']
        # 元素的x,y轴的坐标
        el_location = el.location
        el_x = el_location['x']
        el_y = el_location['y']  # 起止点的y值
        swipe_y1 = el_y * 0.7
        swipe_x = int(el_x + el_width * 0.5)
        swipe_y = int(el_y + el_height * 0.9)  # 最大的y值
        if dir == 'up':
            print('向上滑动，x值不变，y值在变小')
            # 通过循环实现n次滑动
            for i in range(n):
                self.driver.swipe(swipe_x, swipe_y, swipe_x, el_y, 8000)  # 8000是持续时间
                time.sleep(2)  # 模拟人操作，滑动一次停顿一下，否则程序会报错
        elif dir == 'down':
            print('向下滑动，x值不变，y值在变大')
            for i in range(n):
                self.driver.swipe(swipe_x, el_y, swipe_x, swipe_y, 8000)  # 8000是持续时间
                time.sleep(2)
        else:
            raise Exception

    # 选择个人出生年月的滑动封装：第二种写法
    # def el_swipe(self, el, n, dir):
        '''
        size返回的是宽高，location返回的是x,y坐标位置
        :param el: 在el元素这个范围进行滑动
        :param n: 滑动的次数
        :param flag: 滑动的方向 1:swipe_up,-1:swipe_down
        :return:
        '''
        # 获取元素的宽高
        # el_size = el.size
        # el_width = el_size['width']
        # el_height = el_size['height']
        # # 获取元素的x,y坐标
        # el_location = el.location
        # el_x = el_location['x']
        # el_y = el_location['y']
        # swipe_x1 = int((el_x + el_width) * 0.9)
        # swipe_y1 = el_y
        # swipe_y2 = int((el_y + el_height) * 0.9)
        # if dir == -1:
        #     print('{}元素开始向下滑动'.format(el))
        #     for i in range(n):
        #         self.driver.swipe(swipe_x1, swipe_y1, swipe_x1, swipe_y2, 3500)
        #         time.sleep(1)
        # else:
        #     print('{}元素开始向上滑动'.format(el))
        #     for i in range(n):
        #         self.driver.swipe(swipe_x1, swipe_y2, swipe_x1, swipe_y1, 3500)
        #         time.sleep(1)




