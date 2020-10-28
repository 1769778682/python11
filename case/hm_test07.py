import unittest


class Test07(unittest.TestCase):
    """测试类07"""

    def test_method01(self):
        """测试方法01"""
        print('测试类07->测试方法01')

    def test_method02(self):
        """测试方法02"""
        num = 1 / 0  # 模拟错误
        print('测试类07->测试方法02', num)


if __name__ == '__main__':
    unittest.main()
