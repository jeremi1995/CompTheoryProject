from automaton import AutomatonResult

class TestCase:
    caseId: str
    input_string: str
    expected_result: AutomatonResult
    def __init__(self, caseId: str, input_string: str, expected_result: AutomatonResult):
        self.caseId = caseId
        self.input_string = input_string
        self.expected_result = expected_result
