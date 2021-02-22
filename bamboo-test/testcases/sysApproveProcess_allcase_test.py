# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\sysApproveProcess_allcase.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testapi.sysApproveProcess_test import (
    TestCaseSysapproveprocess as Sysapproveprocess,
)


class TestCaseSysapproveprocessAllcase(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "sysApproveProcessType-spu-spuid-needPresale-needInfringement-type": [
                    ["先发布-设计款-首次发布", "SPF1VLRUE2J", "1362960215432306689", 1, 1, 1],
                    ["先发布-扒图款-首次发布", "SPW1JSHN667", "1362960222839447554", 1, 1, 1],
                    ["先发布-设计款-首次发布", "SPF1VLRUE2J", "1362960215432306689", 1, 1, 2],
                    ["先发布-扒图款-首次发布", "SPW1JSHN667", "1362960222839447554", 1, 1, 2],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("测试查询")

    teststeps = [
        Step(RunTestCase("查询测试状态参数化").call(Sysapproveprocess)),
    ]


if __name__ == "__main__":
    TestCaseSysapproveprocessAllcase().test_start()
