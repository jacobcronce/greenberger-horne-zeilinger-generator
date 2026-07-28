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
    statevector = results.simulate_statevector(circuit)
    density_matrix = results.simulate_density_matrix(circuit)
    print("Statevector: ")
    print(statevector)
    print("\n Density Matrix: ")
    print(density_matrix)
    dm_from_sv = results.density_matrix_from_statevector(statevector)
    print("\n Density Matrix from Statevector: ")
    print(dm_from_sv)

    #Fidelity
    fid = results.fidelity(dm_from_sv, density_matrix)
    print("\n Fidelity: ")
    print(fid)

    #Von Neumann Entropy
    entropy = results.von_neumann_entropy(density_matrix)
    print("\n Von Neumann Entropy: ")
    print(entropy)

    #Purity
    purity = results.purity(density_matrix)
    print(np.real(purity))

    #Trace Distance
    trace_dist = results.trace_distance(dm_from_sv, density_matrix)
    print("\n Trace Distance: ")
    print(trace_dist)

    #Check if valid density matrix
    valid = results.is_density_matrix(density_matrix)
    print("\n Is Valid Density Matrix: ")
    print(valid)

    #Partial Trace
    num_qubits = len(circuit.all_qubits())

    if num_qubits > 1:
        reduced_dm = results.partial_trace(
            density_matrix,
            keep=[0],
            num_qubits=num_qubits
        )

        print("\nReduced Density Matrix:")
        print(reduced_dm)
    



elif(permchoice == 2):
    creator.create_trapped_ion_circuit()
    circuit = creator.get_circuit()
elif(permchoice == 3):
    creator.create_neutral_atom_circuit()
    circuit = creator.get_circuit()
else:
    creator.create_photonic_circuit()
    circuit = creator.get_circuit()

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
