from test_case import TestCase

def get_test_cases_dfa():
    return [
        # Should accept
        TestCase("DFA_1", "a", True),
        TestCase("DFA_2", "abbab", True),
        TestCase("DFA_3", "bb", True),
        TestCase("DFA_4", "ba", True),
        TestCase("DFA_5", "babbaabbababababbaabaaaa", True),

        # Should reject
        TestCase("DFA_6", "", False),
        TestCase("DFA_7", "b", False),
        TestCase("DFA_8", "bc", False),
        TestCase("DFA_9", "bac", False),
        TestCase("DFA_10", "ac", False),
    ]

def get_test_cases_nfa():
    return [
        # Should accept
        TestCase("NFA_1", "aa", True),
        TestCase("NFA_2", "ba", True),
        TestCase("NFA_3", "baa", True),
        TestCase("NFA_4", "abaaabbbabb", True),
        TestCase("NFA_5", "bbbbba", True),

        # Should reject
        TestCase("DFA_6", "b", False),
        TestCase("DFA_7", "a", False),
        TestCase("DFA_8", "baabaa", False),
        TestCase("DFA_9", "bbbbaa", False),
        TestCase("DFA_10", "aaa", False),
    ]