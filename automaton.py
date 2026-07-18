from enum import Enum

class AutomatonResult(Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"

class AutomatonType(Enum):
    NFA = "NFA"
    DFA = "DFA"

class StateType(Enum):
    START = "START"
    ACCEPT = "ACCEPT"
    INTERMEDIATE = "INTERMEDIATE"

class Transition:
    start: str
    end: str
    symbols: set[str]
    def __init__(self, start: str, end: str, symbols: set[str]):
        self.start = start
        self.end = end
        self.symbols = symbols
    
    def to_string(self):
        return f"{self.start}--{self.symbols}-->{self.end}"

class State:
    name: str
    type: StateType
    def __init__(self, name: str, type: StateType):
        self.name = name
        self.type = type

class Automaton:
    # a state is a tuple of the state
    _states = list[State]
    _state_name_set = set[str]
    _transitions: list[Transition]
    _alphabet: set[str]
    _state_out_transitions_map: dict[str, set[Transition]]
    _type: AutomatonType

    # constructor
    def __init__(self, states: list[State], transitions: list[Transition], alphabet: set[str], type: AutomatonType):
        self._states = states
        self._state_name_set = set([x.name for x in self._states])
        self._transitions = transitions
        self._alphabet = alphabet
        self._type = type
        self._state_out_transitions_map = self._gen_state_out_transitions_map()
        self.validate_automaton()
        self.display_state_out_transitions_map()

    def _gen_state_out_transitions_map(self):
        resultingMap = {}
        for state in self._states:
            resultingMap[state.name] = [x for x in self._transitions if x.start == state.name]
        return resultingMap
        
    
    def display_state_out_transitions_map(self):
        print("Init: Automaton state-out-transitions map:")
        for key, transitionList in self._state_out_transitions_map.items():
            print(f"{key}: {[x.to_string() for x in transitionList]}")

    def display_automaton(self):
        print("---- Automaton ----")
        print("-- States --")
        for state in self._states:
            print(f"State({state.name}, {state.type})")
        print("-- Transitions --")
        for transition in self._transitions:
            print(f"Transition({transition.to_string()})")
        print("------------------")

    def validate_automaton(self):
        if self._type == AutomatonType.NFA:
            self._validate_nfa()
        elif self._type == AutomatonType.DFA:
            self._validate_dfa()
        else:
            assert False, "INVALID AUTOMATON TYPE!"

    def _validate_dfa(self):
        start_state_count = 0
        accept_state_count = 0
        for state in self._states:
            if state.type == StateType.START:
                start_state_count += 1
            if state.type == StateType.ACCEPT:
                accept_state_count += 1
        assert start_state_count == 1, "DFA must have exactly 1 start state!"
        assert accept_state_count > 0, "DFA must have at least 1 accept state!"
        assert self._alphabet != None, "DFA must have an alphabet!"
        # At every state, there's exactly 1 outgoing transition for each symbol of the alphabet
        transition_duplications = []
        for stateTransitions in self._state_out_transitions_map.values():
            for symbol in self._alphabet:
                transitions_for_symbol = []
                for transition in stateTransitions:
                    if symbol in transition.symbols:
                        transitions_for_symbol.append(f"{transition.to_string()}")
                if len(transitions_for_symbol) > len(self._alphabet):
                    transition_duplications.append(transitions_for_symbol)
        assert len(transition_duplications) == 0, f"DFA must NOT have duplicated outgoing symbol from any state. Duplications: {transition_duplications}"
        # No epsilon transition
        epsilon_transitions = [x.to_string() for x in self._transitions if "eps" in x.symbols]
        assert len(epsilon_transitions) == 0, f"DFA must NOT have any epsilon transitions. Epsilon transitions: {epsilon_transitions}"

    def _validate_nfa(self):
        # Has exactly on start state
        # Has a set of accept states
        start_state_count = 0
        accept_state_count = 0
        for state in self._states:
            if state.type == StateType.START:
                start_state_count += 1
            if state.type == StateType.ACCEPT:
                accept_state_count += 1
        assert start_state_count == 1, "DFA must have exactly 1 start state!"
        assert accept_state_count > 0, "DFA must have at least 1 accept state!"
        # Has a defined alphabet
        assert self._alphabet != None, "DFA must have an alphabet!"
        # No transition for symbols not in alphabet
        # Epsilon transition
        pass


    def process_input(self, inputString: str):
        return AutomatonResult.ACCEPT