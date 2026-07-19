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
    state_out_transitions_map: dict[str, set[Transition]]
    type: AutomatonType

    # constructor
    def __init__(self, states: list[State], transitions: list[Transition], alphabet: set[str], type: AutomatonType):
        self.states = states
        self.state_name_set = set([x.name for x in self.states])
        self.transitions = transitions
        self.alphabet = alphabet
        self.type = type
        self.state_out_transitions_map = self._gen_state_out_transitions_map()
        self.display_state_out_transitions_map()

    def _gen_state_out_transitions_map(self):
        resultingMap = {}
        for state in self.states:
            resultingMap[state.name] = [x for x in self.transitions if x.start == state.name]
        return resultingMap
        
    
    def display_state_out_transitions_map(self):
        print(f"{self.type.value} Initialized: Automaton state-out-transitions map:")
        for key, transitionList in self.state_out_transitions_map.items():
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

    def process_input(self, inputString: str):
        # Add code here to walk the input
        return AutomatonResult.ACCEPT