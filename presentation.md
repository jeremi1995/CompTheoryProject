# Slide 1 — Title

**CISC 603 Final Project**
Finite Automata Simulator: DFA & NFA

Jeremy [Last Name]
July 19, 2026

---

# Slide 2 — Language Description

## DFA Language

**Description:** All non-empty strings over {a, b} except the single character "b".
In other words: any string that starts with 'a', OR starts with 'b' followed by at least one more character.

**Regular Expression:** `a(a+b)* + b(a+b)+`

| Accepted | Rejected |
|----------|----------|
| `a` | ε (empty string) |
| `bb` | `b` |
| `ba` | `bc` (invalid symbol) |
| `abbab` | `bac` (invalid symbol) |

---

## NFA Language

**Description:** Strings over {a, b} that match either:
- The exact string "aa", OR
- Strings of the form: zero or more a's, then b, then zero or more a's, then zero or more b's, then a, then zero or more b's

**Regular Expression:** `aa + a*ba*b*ab*`

| Accepted | Rejected |
|----------|----------|
| `aa` | `a` |
| `ba` | `b` |
| `baa` | `aaa` |
| `bbbbba` | `baabaa` |

---

# Slide 3 — Transition Graphs

## DFA

```
         a
    ┌─────────────────────────┐
    │                         ▼
  ─►q0 ──a──► q2(accept) ◄──a,b──┐
    │                             │
    └──b──► q1 ──a,b──────────────┘
```

States: q0 (start), q1, q2 (accept)
Alphabet: {a, b}

| From | Symbol | To |
|------|--------|----|
| q0 | a | q2 |
| q0 | b | q1 |
| q1 | a, b | q2 |
| q2 | a, b | q2 |

---

## NFA

States: q0 (start), q1, q2, q3, q4 (accept), q5, q6, q7 (accept)
Alphabet: {a, b}, ε (epsilon)

```
                  a(loop)
                  ┌─┐
  ─►q0 ──ε──► q1 ─┘ ──b──► q2 ──ε──► q3 ──a──► q4(accept)
    │              a(loop)       b(loop)      b(loop)
    │
    └───ε──► q5 ──a──► q6 ──a──► q7(accept)
```

| From | Symbol | To |
|------|--------|----|
| q0 | ε | q1 |
| q0 | ε | q5 |
| q1 | a | q1 |
| q1 | b | q2 |
| q2 | a | q2 |
| q2 | ε | q3 |
| q3 | b | q3 |
| q3 | a | q4 |
| q4 | b | q4 |
| q5 | a | q6 |
| q6 | a | q7 |

---

# Slide 4 — Software Implementation

**Language:** Python 3.14

**Libraries/Tools:**
- No external libraries — built entirely with Python standard library
- `enum` module for `AutomatonType`, `StateType`, and `AutomatonResult`

**Architecture:**
- `automaton.py` — Core `Automaton` class implementing both DFA and NFA simulation, `State`, `Transition`, and `NFAExecutionBranch` data classes
- `dfa/dfa.py` — DFA definition; `dfa/validator.py` — DFA validation (checks for exactly one outgoing transition per symbol per state, no epsilon transitions)
- `nfa/nfa.py` — NFA definition; `nfa/validator.py` — NFA validation
- `test_cases/` — Test case definitions and loader
- `main.py` — Entry point, runs all test cases and prints color-coded results

**Key NFA implementation detail:**
The NFA uses a branching simulation approach — each non-deterministic choice spawns a new `NFAExecutionBranch`. A visited set of `(state, remaining_input)` pairs prevents infinite loops caused by epsilon cycles.

---

# Slide 5 — Accepted Strings (Screenshots)

> **TODO:** Run `python main.py` and take screenshots showing:
> 1. DFA accepting `"a"` and `"abbab"`
> 2. NFA accepting `"aa"` and `"ba"`

*(Insert screenshots here)*

---

# Slide 6 — Rejected Strings (Screenshots)

> **TODO:** Run `python main.py` and take screenshots showing:
> 1. DFA rejecting `""` (empty string) and `"b"`
> 2. NFA rejecting `"a"` and `"b"`

*(Insert screenshots here)*

---

# Slide 7 — References

- Python 3.14 Documentation: https://docs.python.org/3/
- Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning.
- Source code: https://github.com/jeremi1995/CompTheoryProject
