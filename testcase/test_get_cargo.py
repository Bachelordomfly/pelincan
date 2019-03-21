# -*- coding:utf-8 -*-
import unittest
from page_element import page_gc, page_login
from selenium import webdriver
from pymongo import MongoClient
import time
from config import log
import random
from selenium.webdriver.support import expected_conditions as EC


class GetCargo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://192.168.1.79:8080'
        # self.url = 'http://120.27.198.114:8989/LdxSmart-0.1'
        # self. client = MongoClient('120.27.198.114', 27017, connect=False)
        self. client = MongoClient('192.168.1.79', 27017, connect=False)
        self.name = 'SZCR'
        self.passwd = '123456'
        self.title = u'用户登录_EXSOFT'
        # self.gc_title = u'收货'
        self.login_page = page_login.loginIn(self.driver)
        self.gc = page_gc.GCPage(self.driver)
        self.mylog = log.log()

    def tearDown(self):
        self.driver.quit()

    def test_gc_01(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('hq080')
        self.gc.cus_code_enter('hq020')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(str(waybill))
        self.gc.product_select(1)
        self.gc.cargotype_select(1)
        self.gc.subwaybill_enter(sub_waybill=waybill+'01')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()

        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'客户不存在'
        while result:
            self.assertIn(result.text, tip1, msg=u'输入错误的客户名称未弹出客户不存在提示信息')

    def test_gc_02(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('hq080')
        self.gc.cus_code_enter('hq020')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(str(waybill))
        self.gc.product_select(1)
        self.gc.cargotype_select(1)
        self.gc.subwaybill_enter(sub_waybill=waybill+'01')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()

        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'客户不存在'
        while result:
            self.assertIn(result.text, tip1, msg=u'输入错误的客户代码未弹出客户不存在提示信息')

    def test_gc_03(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('HQ080')
        self.gc.cus_code_enter('HQ080')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(str(waybill))
        # self.gc.product_select(1)
        self.gc.cargotype_select(1)
        self.gc.subwaybill_enter(sub_waybill=waybill+'01')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()

        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'信息不可为空'
        while result:
            self.assertIn(result.text, tip1, msg=u'未选择产品未弹出信息不可为空提示信息')

    def test_gc_04(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('HQ080')
        self.gc.cus_code_enter('HQ080')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(str(waybill))
        self.gc.product_select(1)
        # self.gc.cargotype_select(1)
        self.gc.subwaybill_enter(sub_waybill=waybill+'01')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()

        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'信息不可为空'
        while result:
            self.assertIn(result.text, tip1, msg=u'未选择货物类型未弹出信息不可为空提示信息')

    def test_gc_05(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('HQ080')
        self.gc.cus_code_enter('HQ080')
        waybill = '20190313001'
        self.gc.waybill_enter(str(waybill))
        self.gc.product_select(1)
        self.gc.cargotype_select(1)
        self.gc.subwaybill_enter(sub_waybill=waybill+'01')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()

        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'单号已存在'
        while result:
            self.assertIn(result.text, tip1, msg=u'输入已存在的单号未弹出单号已存在提示信息')

    def test_gc_06(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('HQ080')
        self.gc.cus_code_enter('HQ080')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(str(waybill))
        self.gc.product_select(1)
        self.gc.cargotype_select(1)
        self.gc.pieces_enter(0)
        self.gc.subwaybill_enter(sub_waybill=waybill+'01')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()
        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'件数应大于0'
        while result:
            self.assertIn(result.text, tip1, msg=u'输入件数0未弹出件数应大于0提示信息')
            result.accept()

        time.sleep(4)
        self.gc.pieces_enter(301)

        value_num = []
        for i in range(20000, 20301):
            tip_num = []
            sub_waybill = i
            weight = random.randint(0, 50)
            length = random.randint(20, 200)
            width = random.randint(20, 200)
            height = random.randint(20, 200)
            tip_num.append(sub_waybill)
            tip_num.append(weight)
            tip_num.append(length)
            tip_num.append(width)
            tip_num.append(height)
            value_num.append(tip_num)
        self.gc.get_table_content(self.driver, value_num)
        self.gc.save_click()
        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'必须大于等于0小于等于300'
        while result:
            self.assertIn(result.text, tip1, msg=u'输入件数301未弹出件数必须大于等于0小于等于300提示信息')
            result.accept()

    def test_gc_07(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('HQ080')
        self.gc.cus_code_enter('HQ020')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(waybill)
        self.gc.product_select(1)
        self.gc.cargotype_select(1)
        pieces = 3
        self.gc.pieces_enter(pieces)
        self.gc.subwaybill_enter(sub_waybill='20190313')
        self.gc.subweight_enter(weight='2.3')
        self.gc.save_click()
        # 判断是否有弹出框
        result = EC.alert_is_present()(self.driver)
        tip1 = u'子单已存在'
        while result:
            self.assertIn(result.text, tip1, msg=u'输入已存在的子单未弹出子单已存在提示')
            result.accept()

    def test_gc_08(self):
        # 登录
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert self.title in self.driver.title, u'title not same'
        except Exception as e:
            self.mylog.error(u'未能正确打开页面:' + self.url)
            print(e)
        self.login_page.input_name(self.name)
        self.login_page.input_passwd(self.passwd)
        self.login_page.click_submit()
        time.sleep(3)

        # 进入收货页面
        self.gc.gc_enter()

        # 输入客户名称
        self.gc.cus_name_enter('HQ080')
        self.gc.cus_code_enter('HQ020')
        waybill = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.gc.waybill_enter(waybill)
        self.gc.product_select(1)
        self.gc.cargotype_select(1)
        pieces = 3
        self.gc.pieces_enter(pieces)
        row_num = self.gc.get_table_row(self.driver)
        self.assertEqual(row_num, pieces, u'件数输入框回车后与子单号输入框数量不一致')
