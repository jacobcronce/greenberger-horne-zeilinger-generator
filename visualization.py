import cirq
import matplotlib.pyplot as plt
import seaborn

class Visualization:

    def __init__(self, circuit, qubits):
        self.circuit = circuit
        self.qubits = qubits
    
    def attempt_visualization(self):
        circuit2 = self.circuit.copy()
        circuit2.append(cirq.measure(self.qubits))
        sim = cirq.Simulator()
        result = sim.run(circuit2, repetitions=1000)
        hist = cirq.plot_state_histogram(result, plt.subplot(), title = 'Qubit States', xlabel = 'States', ylabel = 'Occurrences', tick_label=['000', '001', '010', '011', '100', '101', '110', '111'])
        plt.show()