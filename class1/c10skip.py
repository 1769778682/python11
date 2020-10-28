import unittest

version = 45


class Test(unittest.TestCase):
    # 方法一
    @unittest.skip('代码未完成')
    def test_func1(self):
        print('测试方法1')

    # 方法二：
    @unittest.skipIf(version <= 45, '当前版本不执行')
    def test_func2(self):
        print('测试方法2')

    def test_func3(self):
        print('测试方法3')


if __name__ == '__main__':
    unittest.main()
