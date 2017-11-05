import unittest
import requests
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
# from db_fixture import test_data


class UserSignTest(unittest.TestCase):
    '''用户签到'''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/user_sign/"

    def tearDown(self):
        print(self.result)

    def test_user_sign_all_null(self):
        '''参数为空'''

        payload = {'eid': '', 'phone': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_user_sign_eid_error(self):
        '''eid=901，查询结果不存在'''
        payload = {'eid': 901, 'phone': 13511001102}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'event id is not exists')

    def test_user_sign_status_close(self):
        '''eid=3,发布会状态关闭'''
        payload = {'eid': 3, 'phone': 13511001102}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'event status is not available')

    # def test_user_sign_time_start(self):
    #     '''eid=4,发布会已开始'''
    #     payload = {'eid': 4, 'phone': 13511001102}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 10028)
    #     self.assertEqual(self.result['message'], 'event has started')

    def test_user_sign_phone_error(self):
        '''phone = 13350126000，手机号不存在'''
        payload = {'eid': 1, 'phone': 13350126000}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10031)
        self.assertEqual(self.result['message'], 'user phone null')

    def test_user_sign_eid_phone_error(self):
        '''eid=1，phone=13511001102,手机号和发布会id不匹配'''
        payload = {'eid': 1, 'phone': 13511001102}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10032)
        self.assertEqual(self.result['message'], 'user did not participate in the conference')

    def test_user_sign_has_sign_in(self):
        '''eid =1,phone=13511001101，该用户已签到'''
        payload = {'eid': 1, 'phone': 13511001101}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10033)
        self.assertEqual(self.result['message'], 'user has sign in')

    def test_user_sign_success(self):
        '''eid=1,phone=13511001100,可以成功签到'''
        payload = {'eid': 5, 'phone': 13511001102}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'sign success')


if __name__ == '__main__':
    '''为什么感觉在这里，初始化数据没起作用？--具体原因暂时还未知
        但是在运行run_tests.py的时候，里面的初始化数据库是起了作用的，所以此处注释掉也不影响run_test.py的运行结果'''
    # test_data.init_data()  # 初始化接口测试数据
    unittest.main()
