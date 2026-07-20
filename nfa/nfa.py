# Author: Duc Anh (Jeremy) Duong
from automaton import State
from automaton import Transition
from automaton import Automaton
from automaton import AutomatonType
from automaton import StateType

def construct_jeremy_project_nfa():
    alphabet = set(["a", "b"])
    states = [
        State("q0", StateType.START),
        State("q1", StateType.INTERMEDIATE),
        State("q2", StateType.INTERMEDIATE),
        State("q3", StateType.INTERMEDIATE),
        State("q4", StateType.ACCEPT),
        State("q5", StateType.INTERMEDIATE),
        State("q6", StateType.INTERMEDIATE),
        State("q7", StateType.ACCEPT) # the diagram says q8 but I realized I skipped 7
    ]
    transitions = [
        Transition("q0", "q1", {"eps"}), # eps = epsilon
        Transition("q1", "q2", {"b"}),
        Transition("q1", "q1", {"a"}),
        Transition("q2", "q2", {"a"}),
        Transition("q2", "q3", {"eps"}),
        Transition("q3", "q3", {"b"}),
        Transition("q3", "q4", {"a"}),
        Transition("q4", "q4", {"b"}),
        Transition("q0", "q5", {"eps"}),
        Transition("q5", "q6", {"a"}),
        Transition("q6", "q7", {"a"}),
    ]
    return Automaton(states, transitions, alphabet, AutomatonType.NFA)
