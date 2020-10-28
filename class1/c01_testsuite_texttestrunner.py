# 1. 导包
import unittest
from class1.c01 import Test1
from class1.c01_testcase import Test2

# 2. 实例化套件对象
suite = unittest.TestSuite()  # 注意: 类实例化对象, 语法格式为: 类名()
# 3. 调用方法组装 TestCase
# 方法一: 逐类逐个方法添加 suite.addTest(测试类名('测试方法名'))
suite.addTest(Test1('test_add1'))  # 测试类使用自动导包, 负责测试类名爆红
suite.addTest(Test1('test_add2'))

# 方法二: 逐类添加多个方法 suite.addTest(unittest.makeSuite(测试类名))
suite.addTest(unittest.makeSuite(Test2))  # 注意: makeSuite 没有代码提示, 但是方法可用
# 注意:
# 1. TestSuite 只具备组装 TestCase 的作用, 因此当前代码执行没有任何结果
# 2. TestSuite 组装 TestCase 的方法虽然有两种, 根据具体需求, 任选一种使用即可


# 1. 导包
# 注意: 由于测试执行(TextTestRunner)代码一般会和测试套件(TestSuite)代码写在一起, 因此导包步骤可以省略
# 2. 实例化执行对象
runner = unittest.TextTestRunner()  # 注意: 类实例化对象, 语法格式为: 类名()
# 3. 调用方法执行 TestSuite
# 语法: runner.run(套件对象)
runner.run(suite)
