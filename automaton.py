# Author: Duc Anh (Jeremy) Duong
from enum import Enum

DEAD_STATE = "qDead"

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

class NFAExecutionBranch:
    index: int
    state_sequence: list[str]
    remaining_input: str
    halted: bool
    def __init__(self, index: int, state_sequence: list[str], remaining_input: str, halted: bool):
        self.index = index
        self.state_sequence = state_sequence
        self.remaining_input = remaining_input
        self.halted = halted

class Automaton:
    # a state is a tuple of the state
    states = list[State]
    state_name_set = set[str]
    transitions: list[Transition]
    alphabet: set[str]
    st_map: dict[str, set[Transition]]
    s_map: dict[str, State]
    type: AutomatonType
    start_state: State
    _accept_states: set[str]

    # constructor
    def __init__(self, states: list[State], transitions: list[Transition], alphabet: set[str], type: AutomatonType):
        self.states = states
        self.state_name_set = set([x.name for x in self.states])
        self.transitions = transitions
        self.alphabet = alphabet
        self.type = type
        self.start_state = next((x for x in self.states if x.type == StateType.START), None)
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
        current_state = self.start_state
        state_sequence = [current_state.name]
        for c in input_string:
            possible_transitions = self.st_map[current_state.name]
            valid_transition = next((x for x in possible_transitions if c in x.symbols), None)
            if valid_transition == None:
                return (AutomatonResult.REJECT, state_sequence)
            current_state = self.s_map[valid_transition.end]
            state_sequence.append(current_state.name)

        # after traversing the input, accept if current state is an accept state
        if (current_state.name in self._accept_states):
            return (AutomatonResult.ACCEPT, state_sequence)
        else:
            return (AutomatonResult.REJECT, state_sequence)

    def _walk_nfa_with_input(self, input_string: str):
        # Initialize the process with 1 execution branch and a sequence containing start state
        # Branch tupple: (index, current_state_sequence, remaining_input, branch has halted)
        execution_branches = [NFAExecutionBranch(0, [self.start_state.name], input_string, False)]
        all_branch_halted = False
        branch_index = 0
        visited: set[tuple[str, str]] = {(self.start_state.name, input_string)}

        while not all_branch_halted:
            new_branches_to_add = []
            for branch in execution_branches:
                # Only proceed if branch has not halted
                if not branch.halted:
                    c = None if len(branch.remaining_input) == 0 else branch.remaining_input[0]
                    current_state_name = branch.state_sequence[-1] # last state in the state sequence is the current state
                    
                    # Look at all possible transitions:
                    out_transitions = self.st_map[current_state_name]
                    
                    # It's possible to have multiple valid transitions:
                    valid_transitions = [x for x in out_transitions if ((not c == None) and (c in x.symbols)) or "eps" in x.symbols]
                    vt_length = len(valid_transitions)

                    # If there's no more input:
                    if c == None:
                        branch.halted = True
                        if vt_length > 0:
                            for vt in valid_transitions:
                                for symbol in vt.symbols:
                                    # epsilon check here is kinda redundant, but safe than sorry
                                    if symbol == "eps":
                                        key = (vt.end, branch.remaining_input)
                                        if key not in visited:
                                            visited.add(key)
                                            branch_index += 1
                                            new_state_sequence = branch.state_sequence + [vt.end]
                                            new_branches_to_add.append(NFAExecutionBranch(branch_index, new_state_sequence, branch.remaining_input, False))
                    else:
                        if vt_length == 0:
                            # if there's more input but there's no valid transition,
                            # that means we're transitioning to a dead state
                            branch.halted = True
                            branch.state_sequence.append(DEAD_STATE)
                        else:
                            processed_transitions: set[str] = set()
                            current_branch_took_non_eps_transition = False
                            current_remaining_input_copy = branch.remaining_input
                            current_state_sequence_copy = branch.state_sequence.copy()
                            for vt in valid_transitions:
                                for symbol in vt.symbols:
                                    transition_key = f"{symbol}|{vt.end}"
                                    if transition_key not in processed_transitions:
                                        processed_transitions.add(transition_key)
                                        # if epsilon, don't consume output, just spawn new branch
                                        if symbol == "eps":
                                            key = (vt.end, current_remaining_input_copy)
                                            if key not in visited:
                                                visited.add(key)
                                                branch_index += 1
                                                new_state_sequence = current_state_sequence_copy + [vt.end]
                                                new_branches_to_add.append(NFAExecutionBranch(branch_index, new_state_sequence, current_remaining_input_copy, False))
                                        # double check that we only process the input if the symbol of the transition matches
                                        elif symbol == c:
                                            # Use the current branch to process the current non-epsilon transition
                                            if (not current_branch_took_non_eps_transition):
                                                # make the transition: consume the input, then update state sequence
                                                branch.remaining_input = branch.remaining_input[1:]
                                                branch.state_sequence.append(vt.end)
                                                current_branch_took_non_eps_transition = True
                                            # spawn new branch for all other transitions:
                                            else:
                                                # consume the input, then update state sequence, then spawn new branch
                                                branch_index += 1
                                                new_state_sequence = current_state_sequence_copy + [vt.end]
                                                new_remaining_input = current_remaining_input_copy[1:]
                                                new_branches_to_add.append(NFAExecutionBranch(branch_index, new_state_sequence, new_remaining_input, False))
                            if not current_branch_took_non_eps_transition:
                                branch.halted = True
            # add new branch
            execution_branches.extend(new_branches_to_add)
            all_branch_halted = all(x.halted for x in execution_branches)
            # print(f"branchIndex: {branch_index}")

        successful_branch = next((x for x in execution_branches if x.state_sequence[-1] in self._accept_states), None)
        if not successful_branch == None:
            return (AutomatonResult.ACCEPT, successful_branch.state_sequence)
        return (AutomatonResult.REJECT, [])

    def process_input(self, input_string: str):
        if self.type == AutomatonType.DFA:
            return self._walk_dfa_with_input(input_string)
        elif self.type == AutomatonType.NFA:
            return self._walk_nfa_with_input(input_string)
