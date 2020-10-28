# 1.导包
import unittest
# 2.实例化加载对象并调用方法
# discover():测试用例文件存放目录的路径；测试用例文件名前缀
suite = unittest.TestLoader().discover('./class1/case', 'hm*')


# 配合测试执行，执行测试套件

unittest.TextTestRunner().run(suite)


