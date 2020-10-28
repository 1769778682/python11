import unittest


# 定义加法函数
def add(x, y):
    return x + y


class Test1(unittest.TestCase):

    def test_func1(self):
        # 应用：多用于判断是否相等
        # 语法：assertEqual(预期结果, 实际结果)
        # 注意：断言异常类型 AssertionError
        result = add(13, 14)
        self.assertEqual(27, result)


if __name__ == '__main__':
    unittest.main()