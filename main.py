from dfa.dfa import construct_jeremy_project_dfa
from dfa.validator import validate_dfa
from nfa.nfa import construct_jeremy_project_nfa
from nfa.validator import validate_nfa

def main():
    jeremy_dfa = construct_jeremy_project_dfa()
    validate_dfa(jeremy_dfa)
    jeremy_nfa = construct_jeremy_project_nfa()
    validate_nfa(jeremy_nfa)
    test_string = ""
    result = jeremy_dfa.process_input(test_string)
    print(f"result: {result}")


if __name__ == "__main__":
    main()