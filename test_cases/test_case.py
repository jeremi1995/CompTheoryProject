from automaton import AutomatonResult

class TestCase:
    case_id: str
    input_string: str
    expected_result: AutomatonResult
    def __init__(self, case_id: str, input_string: str, expected_result: AutomatonResult):
        self.case_id = case_id
        self.input_string = input_string
        self.expected_result = expected_result
