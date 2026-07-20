# Author: Duc Anh (Jeremy) Duong
from dfa.dfa import construct_jeremy_project_dfa
from dfa.validator import validate_dfa
from nfa.nfa import construct_jeremy_project_nfa
from nfa.validator import validate_nfa
from test_cases.get_test_cases import *
from test_cases.test_case import TestCase
from automaton import Automaton, StateType
from util import color_text

def run_tests(automaton: Automaton, test_cases: list[TestCase]):
    test_results = []
    for test_case in test_cases:
        dfa_result = automaton.process_input(test_case.input_string)
        test_result = "PASSED" if dfa_result[0] == test_case.expected_result else "FAILED"
        test_results.append((test_case.case_id, test_case.input_string, test_case.expected_result.value, dfa_result[0].value, test_result, dfa_result[1]))
    return test_results

def display_tests_result(test_results: list):
    print("TEST RESULTS:")
    for test_result in test_results:
        trc = "green" if test_result[4] == "PASSED" else "red"
        erc = "green" if test_result[2] == AutomatonResult.ACCEPT.value else "red"
        arc = "green" if test_result[3] == AutomatonResult.ACCEPT.value else "red"

        print(f"[{color_text(trc, test_result[4])}] TestId: {color_text("yellow", test_result[0])} | InputString: {color_text("yellow", f"\"{test_result[1]}\"")}")
        print(f"  Expected  : {color_text(erc, test_result[2])}")
        print(f"  Actual    : {color_text(arc, test_result[3])}")
        print(f"  States    : {color_text("yellow", test_result[5])}")

def test_dfa():
    # Construct the DFA and validate it
    jeremy_dfa = construct_jeremy_project_dfa()
    validate_dfa(jeremy_dfa)

    # Load test cases and run process_input on them
    dfa_test_cases = get_test_cases_dfa()
    test_results = run_tests(jeremy_dfa, dfa_test_cases)

    # Display the result
    display_tests_result(test_results)

def test_nfa():
    # Construct the NFA and validate it
    jeremy_nfa = construct_jeremy_project_nfa()
    validate_nfa(jeremy_nfa)

    # Load test cases and run process_input on them
    nfa_test_cases = get_test_cases_nfa()
    test_results = run_tests(jeremy_nfa, nfa_test_cases)

    # Display the result
    display_tests_result(test_results)

def main():
    print("------TESTING BEGINS-----------------------------------")
    test_dfa()
    print("-------------------------------------------------------")
    test_nfa()
    print("----------------------------------TESTING FINISHED!----\n")


if __name__ == "__main__":
    main()