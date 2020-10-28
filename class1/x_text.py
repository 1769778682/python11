import unittest
from parameterized import parameterized


def add(x, y):
    """加法函数"""
    return x + y


class TestAdd(unittest.TestCase):
    """加法测试类"""

    # 方式一：

    @parameterized.expand([(0, 1, 1), (1, 1, 2), (1, 2, 3)])
    def test_add(self, a, b, expect):
        """加法测试方法"""
        result = add(a, b)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
# 说明：通过扩展插件实现参数化之后，之前案例中出现的问题已经全部解决