# NOTE: Generated By HttpRunner v3.1.4
# FROM: test_all.yaml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.publish_design_test import TestCasePublishDesign as PublishDesign

from testcases.saleApprove_test import TestCaseSaleapprove as Saleapprove

from testcases.publish_mapping_test import TestCasePublishMapping as PublishMapping

from testcases.submitInfringementApprove_test import (
    TestCaseSubmitinfringementapprove as Submitinfringementapprove,
)


class TestCaseTestAll(HttpRunner):

    config = Config("创建商品")

    teststeps = [
        Step(RunTestCase("创建设计款").call(PublishDesign)),
        Step(RunTestCase("预售审核").call(Saleapprove)),
        Step(RunTestCase("创建扒图款").call(PublishMapping)),
        Step(RunTestCase("预售审核").call(Saleapprove)),
        Step(RunTestCase("商品审核").call(Submitinfringementapprove)),
        Step(RunTestCase("商品审核").call(Submitinfringementapprove)),
    ]


if __name__ == "__main__":
    TestCaseTestAll().test_start()
