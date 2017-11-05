import unittest
import requests
import os, sys
from db_fixture import test_data


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class AddEventTest(unittest.TestCase):
    '''添加发布会'''

    def setUp(self):
        self.bas_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        '''所有参数都为空'''
        payload = {'eid': '', 'limit': '', 'address': '', 'start_time': ''}
        r = requests.post(self.bas_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        '''id已存在'''
        payload = {'eid': 1, 'name': 'XXX发布会', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2017-08-20 14:00:00'}
        r = requests.post(self.bas_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10020)
        self.assertEqual(self.result['message'], 'event id is already exists')

    def test_add_event_name_exist(self):
        '''名称已存在'''
        payload = {'eid': 6, 'name': '红米Pro发布会', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2017-08-20 14:00:00'}
        r = requests.post(self.bas_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        '''日期格式错误'''
        payload = {'eid': 6, 'name': '一加4手机发布会', 'limit': 2000, 'status': 1, 'address': '深圳宝体',
                   'start_time': '2017'}
        r = requests.post(self.bas_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error', self.result['message'])

    def test_add_event_success(self):
        '''添加手机'''
        payload = {'eid': 6, 'name': '一加4手机发布会', 'limit': 2000, 'address': "深圳宝体",
                   'start_time': '2017-05-10 12:00:00'}
        r = requests.post(self.bas_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == "__main__":
    '''为什么感觉在这里，初始化数据没起作用？--具体原因暂时还未知
            但是在运行run_tests.py的时候，里面的初始化数据库是起了作用的，所以此处注释掉也不影响run_test.py的运行结果'''
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
