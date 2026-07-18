from automaton import Automaton
from automaton import AutomatonType
from automaton import State
from automaton import Transition
from dfa.dfa import construct_jeremy_project_dfa
from nfa.nfa import construct_jeremy_project_nfa

def main():
    jeremy_dfa = construct_jeremy_project_dfa()
    test_string = ""
    result = jeremy_dfa.process_input(test_string)
    print(f"result: {result}")


if __name__ == "__main__":
    main()