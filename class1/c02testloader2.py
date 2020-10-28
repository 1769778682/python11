# 1.导包
import unittest
# 2.实例化加载对象并调用方法
# discover():测试用例文件存放目录的路径；测试用例文件名前缀
# suite = unittest.TestLoader().discover('./class1/case', 'hm*')
suite = unittest.defaultTestLoader.discover('../case', 'hm*')  # 推荐方法

# 配合测试执行，执行测试套件

unittest.TextTestRunner().run(suite)


# 扩展：TestCase 命名习惯
# 说明：为了在大量用例存在时能够更加方便的管理及批量加载，TestCase 文件命名习惯如下：
# 命名组成：项目名_功能名.py
# 例如：以TPShop商城项目的登录模块为例，对应的命名应该为：tp_login.py 或者 tpshop_login.py
# 注意：不同公司，习惯不尽相同