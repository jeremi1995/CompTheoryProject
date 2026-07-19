from automaton import Automaton
from automaton import AutomatonType
from automaton import StateType

def validate_dfa(automaton: Automaton):
    assert automaton.type == AutomatonType.DFA, f"validate_dfa: Cannot validate automaton of type {automaton.type}"
    start_state_count = 0
    accept_state_count = 0
    for state in automaton.states:
        if state.type == StateType.START:
            start_state_count += 1
        if state.type == StateType.ACCEPT:
            accept_state_count += 1
    assert start_state_count == 1, "DFA must have exactly 1 start state!"
    assert accept_state_count > 0, "DFA must have at least 1 accept state!"
    assert automaton.alphabet != None, "DFA must have an alphabet!"
    # No epsilon transition
    epsilon_transitions = [x.to_string() for x in automaton.transitions if "eps" in x.symbols]
    assert len(epsilon_transitions) == 0, f"DFA must NOT have any epsilon transitions. Epsilon transitions: {epsilon_transitions}"
    # No invalid symbol on transitions
    transitions_with_invalid_symbol = [x.to_string() for x in automaton.transitions if not x.symbols.issubset(automaton.alphabet)]
    assert len(transitions_with_invalid_symbol) == 0, f"DFA must NOT have transitions with symbols outside of alphabet. Invalid transitions: {transitions_with_invalid_symbol}"
    # At every state, there's exactly 1 outgoing transition for each symbol of the alphabet
    transition_duplications = []
    missing_transitions = []
    for stateName, stateTransitions in automaton.state_out_transitions_map.items():
        for symbol in automaton.alphabet:
            transitions_for_symbol = []
            for transition in stateTransitions:
                if symbol in transition.symbols:
                    transitions_for_symbol.append(f"{transition.to_string()}")
            if len(transitions_for_symbol) > 1:
                transition_duplications.append(transitions_for_symbol)
            elif len(transitions_for_symbol) == 0:
                missing_transitions.append(f"{stateName}--{symbol}-->?")
    assert len(transition_duplications) == 0, f"DFA must NOT have duplicated outgoing symbol from any state. Duplications: {transition_duplications}"
    assert len(missing_transitions) == 0, f"DFA must have exactly 1 outgoing transition for every symbol from every state. Missing transitions: {missing_transitions}"