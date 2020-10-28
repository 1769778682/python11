# Fixture方法级别的调用
import unittest


# 需求1: 现对数据库进行测试步骤实现
# 需求变更2 ：要求只连接一次和断开一次数据库，完成两次查询操作
# 需求变更3：# 需求变更 ：要求只连接一次和断开一次数据库，每次查询前，新增数据，完成查询后清除数据。


class Test(unittest.TestCase):

    def setUp(self) -> None:  # setUp ：建立，系统提供的，一般用来执行测试方法的前置条件
        # print('先执行')
        print('新增测试数据')

    def tearDown(self) -> None:  # tearDown ：拆除，系统提供的，一般用来执行测试方法的后置操作
        # print('后执行')
        print('清除测试数据')

    @classmethod
    def setUpClass(cls) -> None:  # setUpClass ：建立，系统提供的，一般用来执行测试方法的前置条件
        # print('先执行')
        print('连接数据库-类方法')

    @classmethod
    def tearDownClass(cls) -> None:  # tearDownClass ：拆除，系统提供的，一般用来执行测试方法的后置操作
        # print('后执行')
        print('断开连接-类方法')

    def test_func1(self):
        """测试方法1"""
        print('测试方法1')
        # print('连接数据库')
        print('查询数据库-基本查询')
        # print('断开连接')

    def test_func2(self):
        """测试方法2"""
        print('测试方法2')
        # print('连接数据库')
        print('查询数据库-连接查询')
        # print('断开连接')


if __name__ == '__main__':
    unittest.main()

# 问题：当测试步骤基本一致时，一些准备和结束的步骤应该进行适当地抽取
# 说明：
# setUp()和tearDown()能够保证：
# 每一个测试方法执行前先执行setUp(),再执行测试方法，最后执行tearDown()
# setUpClass() 和 tearDownClass()是类方法，保证：
# 在类中的所有测试方法前执行setUpClass()，所有方法执行完成后再执行tearDownClass()
