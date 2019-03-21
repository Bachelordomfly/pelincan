# coding:utf-8
import unittest, time
from runcase import HTMLTestReportCN
from config.globalparameter import test_case_path, report_name
from config import send_email
import testcase
'''
构建测试套件，并执行测试
'''

# def Suite():
#     suiteTest = unittest.TestSuite()
#     suiteTest.addTest(testcase("case1"))
#     suiteTest.addTest(testcase("case2"))
#     suiteTest.addTest(testcase("case3"))
#     return suiteTest


# 构建测试集,包含test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')
# 执行测试
if __name__ == "__main__":
    report = report_name+"Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fb,
        title=u'自动化测试报告',
        description=u'项目描述。………',
        tester=u'jiajia'
    )
    runner.run(suite)
    fb.close()
    # 发送邮件
    time.sleep(10)
    email = send_email.send_email()
    email.sendReport()
