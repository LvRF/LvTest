#ecoding = utf-8

import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):

    #每个用例执行前都会先执行setUp()函数，用例执行完成后都会执行tearDown()函数
    # def setUp(self):
    #     print("do something before test.prepare environment.")
    #
    # def tearDown(self):
    #     print("do something after test.clean up.")

    # setUpClass和tearDownClass在整个测试套中均只执行一次
    @classmethod
    def setUpClass(cls):
        print("this setUpClass() method only called once.")
    @classmethod
    def tearDownClass(cls):
        print("this tearDownClass() method only called once too.")

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))

    def test_minus(self):
        self.assertEqual(1,minus(3,2))

    def test_multi(self):
        self.assertEqual(6,multi(2,3))

    def test_divide(self):
        self.assertEqual(2,divide(6,3))
        self.assertEqual(4,divide(5,2))

    #方法一：使用skip装饰器跳过指定用例不执行
    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        # 方法二：使用TestCase.skipTest()方法
        self.skipTest("Do not run this.")
        print('divide')
        self.assertEqual(2,divide(4,2))
        self.assertEqual(3,divide(5,2))

    # def setUp(self):
    #     print("do something before test.prepare environment.")
    #
    # def tearDown(self):
    #     print("do something after test.clean up.")

if __name__ == '__main__':
    unittest.main()