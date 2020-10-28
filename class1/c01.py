# 需求：定义一个加法计算函数，并对该函数进行测试
# 定义一个加法函数
# 导包
import unittest


# def add_func(x, y):
#     """加法函数"""
#     return x + y


class Test1(unittest.TestCase):
    """加法测试类"""

    def test_add1(self):
        """测试方法"""
        # result = add_func(2, 7)
        # num = 1 / 0  # 模拟器测试执行错误
        print('测试类1->测试方法1', num)

    def test_add2(self):
        # result = add_func(6, 9)
        print(f'测试类1->测试方法2')


if __name__ == '__main__':
    unittest.main()