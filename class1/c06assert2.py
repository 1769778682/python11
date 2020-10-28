import unittest


# 定义加法函数
def add(x, y):
    return x + y


class Test1(unittest.TestCase):

    def test_func1(self):
        # assertIn（'预期结果字符串', '测试结果字符串'）：预期结果字符串是否被测试结果字符串包含
        # 应用：主要用于判断获取的信息字符串的包含关系，如果包含则通过，反之报错
        # 注意：
        # 1.预期结果字符串不能超过测试结果字符串
        # 2.如果预期结果字符串和测试结果字符串完全一致，从断言结果上来看等价于assertEqual
        self.assertIn('admin', 'admin')


if __name__ == '__main__':
    unittest.main()