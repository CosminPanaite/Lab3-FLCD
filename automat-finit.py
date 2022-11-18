import json


class AutomatFinit:
    states = '',
    alphabet = '',
    transition_functions = {}
    initial_state = ''
    final_state = ''

    def __init__(self, json_file):
        f = open(json_file)
        self.json_file = json.load(f)
        self.states = self.json_file['stari']
        self.alphabet = self.json_file['alfabetIntrare']
        self.transition_functions = self.json_file['functiiTranzitie']
        self.initial_state = self.json_file['stareInitiala']
        self.final_state = self.json_file['stariFinale']

    def get_states(self):
        return self.states

    def get_alfabet(self):
        return self.alphabet

    def get_transitions_functions(self):
        return self.transition_functions

    def get_initial_state(self):
        return self.initial_state

    def get_final_state(self):
        return self.final_state


op = True
json_file = ''

while op == True:
    json_file = input("Select the configuration: (I -> Identifiers/C -> Constants): ")
    if json_file == 'I':
        json_file = 'identificatori.json'
        op = False
    elif json_file == 'C':
        json_file = 'constante.json'
        op = False
    else:
        print("Retry please!")

automat_finit = AutomatFinit(json_file)
tranzitii = {}

print("---------------------------------------------------------")
print(f"The set of states: {automat_finit.get_states()}")
print("---------------------------------------------------------")
print(f"The Alphabet: {automat_finit.get_alfabet()}")
print("---------------------------------------------------------")
for tranzitie in automat_finit.get_transitions_functions():
    tranzitii[(tranzitie[0], tranzitie[2])] = tranzitie[1]
    print(f"From {tranzitie[0]} we go to {tranzitie[1]} through {tranzitie[2]}")
print("---------------------------------------------------------")
print(f"Initial state: {automat_finit.get_initial_state()}")
print("---------------------------------------------------------")
print(f"Set of final states: {automat_finit.get_final_state()}")
print("---------------------------------------------------------")

secv = True

while secv:
    input_string = input("Give a sequence for validation: ")
    current_state = automat_finit.get_initial_state()

    for char in input_string:
        print((current_state), char)
        if (current_state, char) in tranzitii.keys():
            current_state = tranzitii[(current_state, char)]
        else:
            print("Refused sequence")
            break

        if current_state is None:
            print("Refused sequence")
            break

    else:
        if current_state in automat_finit.get_final_state():
            print("Accepted sequence")
        else:
            print("Refused sequence")
    opt = True
    while opt:
        redo = input("Do you want another sequence? (Y/N)")
        if redo == 'Y':
            secv = TrueI
            opt = False
        elif redo == 'N':
            secv = False
            opt = False
        else:
            print("Retry please!")

while True:
    stare_citita = input("Give the state: ")
    simbol_citit = input("Give the symbol: ")
    if (stare_citita, simbol_citit) in tranzitii.keys():
        print(f"The state in which it will be reached: {tranzitii[(stare_citita,simbol_citit)]}")
    else:
        print(f"Such transition does not exist")