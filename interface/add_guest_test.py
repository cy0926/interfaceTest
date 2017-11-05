#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import requests
import os, sys
from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class AddGuestTest(unittest.TestCase):
    ''' 添加嘉宾 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_guest/"

    def tearDown(self):
        # print(self.result)
        pass
    def test_add_guest_all_null(self):
        '''参数为空'''
        payload = {'eid': '', 'realname': '', 'phone': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_guest_eid_not_exist(self):
        '''eid=9,查询为空'''
        payload = {'eid': 9, 'realname': 'tom', 'phone': 13350326222}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'event id is not exists')

    def test__add_guest_status_close(self):
        '''eid=3,发布会状态是未开启'''
        payload = {'eid': 3, 'realname': 'tom', 'phone': 13350326222}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_add_guest_limit_full(self):
        '''eid=2,发布会人数已满'''
        payload = {'eid': 2, 'realname': 'tom', 'phone': 13350326222}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10027)
        self.assertEqual(self.result['message'], 'event number is full')

    def test_add_guest_time_start(self):
        '''eid = 4,发布会已经开始'''
        payload = {'eid': 4, 'realname': 'tom', 'phone': 13350326222}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10028)
        self.assertEqual(self.result['message'], 'event has started')

    def test_add_guest_phone_repeat(self):
        '''phone = 13511001100,手机号重复'''
        payload = {'eid': 1, 'realname': 'tom', 'phone': 13511001100}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10029)
        self.assertEqual(self.result['message'], 'the event guest phone number is repeat')

    def test_add_guest_success(self):
        '''添加成功'''
        payload = {'eid': 1, 'realname': 'tom', 'phone': 13511001103}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add guest success')


if __name__ == '__main__':
    '''为什么感觉在这里，初始化数据没起作用？--具体原因暂时还未知
            但是在运行run_tests.py的时候，里面的初始化数据库是起了作用的，所以此处注释掉也不影响run_test.py的运行结果'''
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
