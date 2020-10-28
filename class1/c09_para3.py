import unittest
from parameterized import parameterized


def add(x, y):
    """加法函数"""
    return x + y


class TestAdd(unittest.TestCase):
    """加法测试类"""

    # 方式二：
    # 定义变量接收数据
    test_list = [[0, 1, 1], [1, 1, 2], [1, 2, 3]]

    @parameterized.expand(test_list)
    def test_add(self, a, b, expect):
        """加法测试方法"""
        result = add(a, b)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
