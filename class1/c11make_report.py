# 1.导包
# 注意：一般编写代码时用到什么包导哪个包
import unittest
from report.HTMLTestRunner import HTMLTestRunner

# # 2.生成测试套件
suite = unittest.defaultTestLoader.discover('../case', 'hm*')
# 3.设置报告文件的存放目录和文件名
report_name = '../report/test_report.html'
# 4.打开报告文件
with open(report_name, 'wb') as f:
    # print(f)
    # 5.实例化报告生成对象
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='测试报告',
                            description='测试环境，python 3.6.4'
                            )
# 6.调用测试套件执行方法，生成测试报告
    runner.run(suite)


