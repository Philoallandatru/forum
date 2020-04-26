import unittest
from BSTestRunner import BSTestRunner
import time

# 定义测试用例的路径
test_dir = "."
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    report_dir = "." # 定义存放报告的路径
    now = time.strftime("%y-%m-%d %H_%M_%S")    # 对报告的时间命名格式化
    report_name = report_dir+'/'+now+"_result.html"  # 报告文件的完整路径

    # 打开文件，在报告文件写入测试结果
    with open(report_name,'wb') as f:
        runner = BSTestRunner(stream=f,title="Test Report"+"_Login",description="TestCase Result")
        runner.run(discover)    # 执行测试用例

    f.close()   # 保存后关闭文件