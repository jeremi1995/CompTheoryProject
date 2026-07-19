from automaton import Automaton
from automaton import StateType

def dfa_allowed_symbols(alphabet: set[str]):
    return alphabet.union(set(["eps"]))

def validate_nfa(automaton: Automaton):
    # Has exactly 1 start state
    # Has a set of accept states
    start_state_count = 0
    accept_state_count = 0
    for state in automaton.states:
        if state.type == StateType.START:
            start_state_count += 1
        if state.type == StateType.ACCEPT:
            accept_state_count += 1
    assert start_state_count == 1, "NFA must have exactly 1 start state!"
    assert accept_state_count > 0, "NFA must have at least 1 accept state!"
    # Has a defined alphabet
    assert automaton.alphabet != None, "NFA must have an alphabet!"
    # No invalid symbol on transitions, epsilon is allowed
    transitions_with_invalid_symbol = [x.to_string() for x in automaton.transitions if not x.symbols.issubset(dfa_allowed_symbols(automaton.alphabet))]
    assert len(transitions_with_invalid_symbol) == 0, f"NFA must NOT have transitions with symbols outside of alphabet. Allow: {dfa_allowed_symbols(automaton.alphabet)}. Invalid transitions: {transitions_with_invalid_symbol}"
