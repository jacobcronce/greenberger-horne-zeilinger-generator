import cirq
from noise import Noise
from results import Results
from setup import Setup
import numpy as np

creator = Setup(3)
creator.create_qubits()


permchoice = None
while True:
    choice = int(input("1. Superconducting\n2. Trapped Ion\n3. Neutral Atom\n4. Photonic\n\nChoose a number."))
    if(choice not in [1,2,3,4]):
        pass
    else:
        permchoice = choice
        break

if(permchoice == 1):
    creator.create_superconducting_circuit()
    circuit = creator.get_circuit()
    #Density matrix and statvector
    results = Results()
    #show_results(self, creator, results, circuit)
    results.show_results(creator, results, circuit)
    



elif(permchoice == 2):
    creator.create_trapped_ion_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit)
elif(permchoice == 3):
    creator.create_neutral_atom_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit)
else:
    creator.create_photonic_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit)

'''sim = cirq.Simulator()
findings = sim.run(circuit, repetitions=1000)

for i in range(findings):'''

test = Results()
vec = test.simulate_statevector(circuit)
print(vec)
matrix = test.simulate_density_matrix(circuit)
print(matrix)



#simulate circuit 1000x and for each simulation, measure the qubits and record the results
#perform calculations to determine the fidelity of the GHZ state and the effect of noise on the circuit
#record the results outside of the loop, possibly in another file or in a database, for later analysis and comparison with other architectures
#repeat

#possibly add selection and terminal interface
