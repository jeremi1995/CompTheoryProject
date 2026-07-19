from test_cases.test_case import TestCase
from automaton import AutomatonResult

def get_test_cases_dfa():
    return [
        # Should accept
        TestCase("DFA_1", "a", AutomatonResult.ACCEPT),
        TestCase("DFA_2", "abbab", AutomatonResult.ACCEPT),
        TestCase("DFA_3", "bb", AutomatonResult.ACCEPT),
        TestCase("DFA_4", "ba", AutomatonResult.ACCEPT),
        TestCase("DFA_5", "babbaabbababababbaabaaaa", AutomatonResult.ACCEPT),

        # Should reject
        TestCase("DFA_6", "", AutomatonResult.REJECT),
        TestCase("DFA_7", "b", AutomatonResult.REJECT),
        TestCase("DFA_8", "bc", AutomatonResult.REJECT),
        TestCase("DFA_9", "bac", AutomatonResult.REJECT),
        TestCase("DFA_10", "ac", AutomatonResult.REJECT),
    ]

def get_test_cases_nfa():
    return [
        # Should accept
        TestCase("NFA_1", "aa", AutomatonResult.ACCEPT),
        TestCase("NFA_2", "ba", AutomatonResult.ACCEPT),
        TestCase("NFA_3", "baa", AutomatonResult.ACCEPT),
        TestCase("NFA_4", "abaaabbbabb", AutomatonResult.ACCEPT),
        TestCase("NFA_5", "bbbbba", AutomatonResult.ACCEPT),

        # Should reject
        TestCase("NFA_6", "b", AutomatonResult.REJECT),
        TestCase("NFA_7", "a", AutomatonResult.REJECT),
        TestCase("NFA_8", "baabaa", AutomatonResult.REJECT),
        TestCase("NFA_9", "bbbbaa", AutomatonResult.REJECT),
        TestCase("NFA_10", "aaa", AutomatonResult.REJECT),
    ]