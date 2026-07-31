from results import Results
from setup import Setup
from visualization import Visualization

creator = Setup(3)
creator.create_qubits()

permchoice = None
while True:
    choice = int(input("1. Superconducting\n2. Trapped Ion\n\nChoose a number.\n"))
    if(choice not in [1,2]):
        pass
    else:
        permchoice = choice
        break

if(permchoice == 1):
    creator.create_circuit()
    circuit = creator.get_circuit()
    #Density matrix and statvector
    results = Results()
    #show_results(self, creator, results, circuit)
    results.show_results(creator, results, circuit, False)
elif(permchoice == 2):
    creator.create_circuit()
    circuit = creator.get_circuit()
    results = Results()
    results.show_results(creator, results, circuit, True)

visual = Visualization(circuit, creator.get_qubits(), results.get_density_matrix())
visual.attempt_visualization()
visual.plot_density_matrix()



