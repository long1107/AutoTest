import unittest
from utils import HTMLTestRunner
import time
suite = unittest.defaultTestLoader.discover(start_dir='./cases')

reportname = time.strftime("%Y-%m-%d-%H-%M-%S")
with open("./reports/测试报告-%s.html" % reportname,"wb") as f:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title="测试报告",
        description="执行人：龙冬冬"
    )
    runner.run(suite)

