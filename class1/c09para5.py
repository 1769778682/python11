import unittest
# 1.导包
# from parameterized import parameterized
from parameterized import parameterized


def add(x, y):
    """加法函数"""
    return x + y


def build_test_data():
    return [(0, 1, 1), (1, 1, 2), (1, 2, 3)]


class TestAdd(unittest.TestCase):
    """加法测试类"""

    # 方式三: 在测试类外部定义获取数据的函数，再传入函数名（重点）
    # 注意：函数名的传入，不带括号，也没有任何影响
    # 2. 添加装饰器并调用方法
    @parameterized.expand(build_test_data())  # 3. 传入数据
    def test_add(self, a, b, expect):  # 4. 声明变量完成测试
        """加法测试方法"""
        result = add(a, b)  # 调用待测函数
        self.assertEqual(expect, result)  # 断言判断结果


if __name__ == '__main__':
    unittest.main()
