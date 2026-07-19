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
        symbols_string = ""
        l = len(self.symbols)
        for i, s in enumerate(self.symbols):
            symbols_string += f"{s}{"" if i == l-1 else ","}"
        return f"{self.start}--{symbols_string}-->{self.end}"

class State:
    name: str
    type: StateType
    def __init__(self, name: str, type: StateType):
        self.name = name
        self.type = type

class Automaton:
    # a state is a tuple of the state
    states = list[State]
    state_name_set = set[str]
    transitions: list[Transition]
    alphabet: set[str]
    st_map: dict[str, set[Transition]]
    s_map: dict[str, set[State]]
    type: AutomatonType
    _start_state: State
    _accept_states: set[str]

    # constructor
    def __init__(self, states: list[State], transitions: list[Transition], alphabet: set[str], type: AutomatonType):
        self.states = states
        self.state_name_set = set([x.name for x in self.states])
        self.transitions = transitions
        self.alphabet = alphabet
        self.type = type
        self._start_state = [x for x in self.states if x.type == StateType.START][0]
        self._accept_states = set([x.name for x in self.states if x.type == StateType.ACCEPT])
        self.s_map = self._gen_s_map()
        self.st_map = self._gen_st_map()
        self.display_st_map()

    def _gen_st_map(self):
        resultingMap = {}
        for state in self.states:
            resultingMap[state.name] = [x for x in self.transitions if x.start == state.name]
        return resultingMap
    
    def _gen_s_map(self):
        resultingMap = {}
        for state in self.states:
            resultingMap[state.name] = state
        return resultingMap
        
    
    def display_st_map(self):
        print(f"{self.type.value} Initialized: Automaton states and out-transitions map:")
        print(f"Start state: {self._start_state}")
        print(f"Accept states: {self._accept_states}")
        for key, transitionList in self.st_map.items():
            print(f"{key}: {[x.to_string() for x in transitionList]}")

    def display_automaton(self):
        print("---- Automaton ----")
        print("-- States --")
        for state in self.states:
            print(f"State({state.name}, {state.type})")
        print("-- Transitions --")
        for transition in self.transitions:
            print(f"Transition({transition.to_string()})")
        print("------------------")

    def _walk_dfa_with_input(self, input_string: str):
        current_state = self._start_state
        state_sequence = [current_state.name]
        for c in input_string:
            possible_transitions = self.st_map[current_state.name]
            valid_transition = next((x for x in possible_transitions if c in x.symbols), None)
            if valid_transition == None:
                return (AutomatonResult.REJECT, state_sequence)
            print(f"valid transition: {valid_transition.to_string()}")
            current_state = self.s_map[valid_transition.end]
            print(f"toState: {current_state.name}")
            state_sequence.append(current_state.name)

        # after traversing the input, accept if current state is an accept state
        if (current_state.name in self._accept_states):
            return (AutomatonResult.ACCEPT, state_sequence)
        else:
            return (AutomatonResult.REJECT, state_sequence)

    def _walk_nfa_with_input(self, input_string: str):
        return (AutomatonResult.ACCEPT, [])

    def process_input(self, input_string: str):
        if self.type == AutomatonType.DFA:
            return self._walk_dfa_with_input(input_string)
        elif self.type == AutomatonType.NFA:
            return self._walk_nfa_with_input(input_string)
