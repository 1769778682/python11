import unittest


def setUpModule():
    print('模块级别->开始')


def tearDownModule():
    print('模块级别->结束')


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:  # setUpClass ：建立，系统提供的，一般用来执行测试方法的前置条件
        # print('先执行')
        print('测试类1-类级别-开始')

    @classmethod
    def tearDownClass(cls) -> None:  # tearDownClass ：拆除，系统提供的，一般用来执行测试方法的后置操作
        # print('后执行')
        print('测试类1-类级别-结束')

    def setUp(self) -> None:  # setUp ：建立，系统提供的，一般用来执行测试方法的前置条件
        # print('先执行')
        print('测试类1-方法级别-开始')

    def tearDown(self) -> None:  # tearDown ：拆除，系统提供的，一般用来执行测试方法的后置操作
        # print('后执行')
        print('测试类1-方法级别-结束')

    def test_func1(self):
        print('测试类1-测试方法')


class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:  # setUpClass ：建立，系统提供的，一般用来执行测试方法的前置条件
        # print('先执行')
        print('测试类2-类级别-开始')

    @classmethod
    def tearDownClass(cls) -> None:  # tearDownClass ：拆除，系统提供的，一般用来执行测试方法的后置操作
        # print('后执行')
        print('测试类2-类级别-结束')

    def setUp(self) -> None:  # setUp ：建立，系统提供的，一般用来执行测试方法的前置条件
        # print('先执行')
        print('测试类2-方法级别-开始')

    def tearDown(self) -> None:  # tearDown ：拆除，系统提供的，一般用来执行测试方法的后置操作
        # print('后执行')
        print('测试类2-方法级别-结束')

    def test_func1(self):
        print('测试类2-测试方法')


if __name__ == '__main__':
    unittest.main()
