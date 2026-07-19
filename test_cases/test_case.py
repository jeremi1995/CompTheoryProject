from automaton import AutomatonResult

class TestCase:
    caseId: str
    inputString: str
    expectedResult: AutomatonResult
    def __init__(self, caseId: str, inputString: str, expectedResult: AutomatonResult):
        self.caseId = caseId
        self.inputString = inputString
        self.expectedResult = expectedResult
