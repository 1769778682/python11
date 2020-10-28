import unittest


def add(x, y):
    return x + y


class Test(unittest.TestCase):

    # 整理测试数据
    def test_add(self):
        # 用一个测试方法将所有测试数据全部使用一遍
        test_list = [(0, 1, 1), (1, 1, 1), (1, 2, 3)]
        for i, j, expect in test_list:
            print(i, j, expect)
            result = add(i, j)
            self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()

# 优点：测试方法在中间方法报错时，不会影响后续测试方法继续执行
