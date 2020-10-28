import unittest


def add(x, y):
    return x + y


class Test(unittest.TestCase):

    def test_add01(self):
        result = add(1, 0)
        self.assertEqual(1, result)

    def test_add02(self):
        result = add(1, 1)
        self.assertEqual(1, result)

    def test_add03(self):
        result = add(1, 2)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()

# 优点：测试方法在中间方法报错时，不会影响后续测试方法继续执行