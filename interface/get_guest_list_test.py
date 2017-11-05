import unittest
import requests
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class GetGuestListTest(unittest.TestCase):
    '''获得嘉宾列表'''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_guest_list/"

    def tearDown(self):
        print(self.result)

    def test_get_guest_list_eid_null(self):
        '''eid 参数为空 '''
        r = requests.get(self.base_url, params={'eid': ''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10030)
        self.assertEqual(self.result['message'], 'eid cannot be empty')

    def test_get_event_list_eid_error(self):
        '''根据eid查询结果为空'''
        r = requests.get(self.base_url, params={'eid': 901})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        '''根据eid 查询结果成功'''
        r = requests.get(self.base_url, params={'eid': 1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['realname'], 'alen')
        self.assertEqual(self.result['data'][0]['phone'], '13511001100')

    def test_get_event_list_eid_phone_null(self):
        '''根据eid 和 phone查询结果为空'''
        r = requests.get(self.base_url, params={'eid': 1, 'phone': 100000000})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_phone_success(self):
        '''根据eid和phone查询结果成功'''
        r = requests.get(self.base_url, params={'eid': 5, 'phone': '13511001102'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['realname'], 'tom')
        self.assertEqual(self.result['data']['phone'], '13511001102')


if __name__ == '__main__':
    '''为什么感觉在这里，初始化数据没起作用？--具体原因暂时还未知
            但是在运行run_tests.py的时候，里面的初始化数据库是起了作用的，所以此处注释掉也不影响run_test.py的运行结果'''
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
