class DFA:
    def __init__(self, transition_function, start_state, accepting_states):
        self.transition_function = transition_function
        self.state = start_state
        self.accepting_states = accepting_states

    def run(self, input_string):
        for symbol in input_string:
            self.state = self.transition_function[self.state][symbol]
        return self.state in self.accepting_states

# Example DFA
dfa = DFA(
    {'q0': {'0': 'q1', '1': 'q0'}, 'q1': {'0': 'q2', '1': 'q0'}, 'q2': {'0': 'q2', '1': 'q2'}}, 
    'q0', 
    {'q2'}
)

# Test the DFA
print(dfa.run("001"))  # Output: True (Accepted)
print(dfa.run("011"))  # Output: False (Rejected)
