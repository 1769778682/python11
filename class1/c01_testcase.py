# 需求：定义一个加法计算函数，并对该函数进行测试
# 定义一个加法函数
# 导包
import unittest

#
# def add_func(x, y):
#     """加法函数"""
#     return x + y


class Test2(unittest.TestCase):
    """加法测试类"""

    def test_add(self):
        # result = add_func(2, 7)
        print('测试类2->测试方法1')

    def test_add2(self):
        # result = add_func(6, 9)
        # self.assertTrue(0)  # 模拟测试未通过(测试失败)
        print('测试类2->测试方法2')


if __name__ == '__main__':
    unittest.main()