from results import Results
from setup import Setup
from visualization import Visualization
import numpy as np

creator = Setup(3)
creator.create_qubits()


permchoice = None
while True:
    choice = int(input("1. Superconducting\n2. Trapped Ion\n3. Neutral Atom\n4. Photonic\n\nChoose a number.\n"))
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
    results.show_results(creator, results, circuit, False)
elif(permchoice == 2):
    creator.create_trapped_ion_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit, True)
elif(permchoice == 3):
    creator.create_neutral_atom_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit, False)
else:
    creator.create_photonic_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit, False)

visual = Visualization(circuit, creator.get_qubits(), results.get_density_matrix())
visual.attempt_visualization()
visual.plot_density_matrix()

