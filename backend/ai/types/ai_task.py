from enum import Enum


class AITask(str, Enum):
    TESTCASE = "testcase"
    PLAYWRIGHT = "playwright"
    REPORT = "report"
    EXECUTION = "execution"