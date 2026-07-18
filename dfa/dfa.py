from automaton import State
from automaton import Transition
from automaton import Automaton
from automaton import AutomatonType
from automaton import StateType

def construct_jeremy_project_dfa():
    alphabet = set(["a", "b"])
    states = [
        State("q0", StateType.START),
        State("q1", StateType.INTERMEDIATE),
        State("q2", StateType.ACCEPT)
    ]
    transitions = [
        Transition("q0", "q1", {"b"}),
        Transition("q0", "q2", {"a"}),
        Transition("q1", "q2", {"a", "b"}),
        Transition("q2", "q2", {"a", "b"}),
    ]
    return Automaton(states, transitions, alphabet, AutomatonType.DFA)
