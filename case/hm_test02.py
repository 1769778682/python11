import unittest


class Test02(unittest.TestCase):
    """测试类02"""

    def test_method01(self):
        """测试方法01"""
        self.assertTrue(0)  # 模拟失败
        print('测试类02->测试方法01')

    def test_method02(self):
        """测试方法02"""
        print('测试类02->测试方法02')


if __name__ == '__main__':
    unittest.main()
