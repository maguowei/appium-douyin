import time
import os
import random
import copy
from appium import webdriver


IOS_BASE_CAPS = {
    'platformName': 'iOS',
    'platformVersion': '13.1',
    'automationName': 'xcuitest',
    'deviceName': 'My iPhone',
    'bundleId': 'com.ss.iphone.ugc.Aweme',
    # 'bundleId': 'com.zhihu.ios',
    'udid': os.environ.get('udid'),
    'xcodeOrgId': os.environ.get('xcodeOrgId'),
    'xcodeSigningId': 'iPhone Developer',
    'printPageSourceOnFindFailure': True,
    'autoAcceptAlerts': True,
}

HOT_CITY = ['成都', '西安', '杭州', '合肥', '北京', '广州', '苏州', '郑州', '长沙', '上海', '重庆', '武汉', '南京', '福州', '深圳']


desired_caps = copy.copy(IOS_BASE_CAPS)


class DouyinDriver:

    # Nav
    SEARCH = '搜索'
    NEARBY = '北京'

    # TabBar
    HOME = '首页'
    FOLLWERS = '关注'
    ME = '我'
    LOCAL = '同城'

    def __init__(self, desired_caps):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.size = self.driver.get_window_size()
        self.start_x = self.size['width'] / 2
        self.start_y = self.size['height'] * 0.3
        self.end_y = self.size['height'] * 0.2
        time.sleep(5)

    def followers(self):
        self.click_by_name(DouyinDriver.FOLLWERS)
        self.do_forever(self.scroll)

    def go_star_list(self):
        self.click_by_name(DouyinDriver.SEARCH)
        self.click_by_name('明星爱DOU榜')
        self.click_by_name('已入驻1363位明星')
        self.do_forever(self.scroll)

    def go_to_city(self, name):
        self.click_by_name('切换')
        self.click_by_name(name)
        self.do_forever(self.scroll)

    def do_forever_loc(self, action):
        num = 0
        while True:
            num += 1
            if num > 1000:
                self.click_by_name('切换')
                time.sleep(2)
                self.click_by_name(random.choice(HOT_CITY))
                num = 0
            print('action to do....')
            action()
            time.sleep(2)
            # print(self.driver.page_source)
            print('action done!')

    def do_forever(self, action):
        while True:
            print('action to do....')
            action()
            # time.sleep(2)
            # print(self.driver.page_source)
            print('action done!')

    def scroll(self):
        """快速向上滚动
        """
        self.driver.swipe(self.start_x, self.start_y, self.start_x, self.end_y, 50)

    def scroll_down(self):
        """向上滚动"""
        self.driver.execute_script('mobile:scroll', {'direction': 'down'})

    def pull(self):
        """下拉
        """
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})

    def swipe_up(self):
        """向上滑动
        """
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def click_by_name(self, name):
        e = self.find_element_by_name(name)
        e.click()


if __name__ == '__main__':
    d = DouyinDriver(desired_caps)
    # d.click_by_name(DouyinDriver.ME)
    # d.click_by_name(DouyinDriver.FOLLWERS)
    # d.do_forever(d.swipe_up)
    d.do_forever_loc(d.pull)
