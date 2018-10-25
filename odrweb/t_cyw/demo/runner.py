# coding=utf-8
from odrweb.core.initrunner import TestRunner
from time import sleep
for i in range(0, 10):
    if __name__ == '__main__':
        runner = TestRunner()
        runner.run()
        sleep(2)
        print("---------------第" + str(i+1) + "次结束---------------")
