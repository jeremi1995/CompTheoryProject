class TestCase:
    caseId: str
    inputString: str
    expectPass: bool
    def __init__(self, caseId: str, inputString: str, expectPass: bool):
        self.caseId = caseId
        self.inputString = inputString
        self.expectPass = expectPass
