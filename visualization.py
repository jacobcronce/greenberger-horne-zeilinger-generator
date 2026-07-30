import cirq
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Visualization:

    def __init__(self, circuit, qubits, density_matrix):
        self.circuit = circuit
        self.qubits = qubits
        self.density_matrix = density_matrix
    
    def attempt_visualization(self):
        circuit2 = self.circuit.copy()
        circuit2.append(cirq.measure(self.qubits))
        sim = cirq.Simulator()
        result = sim.run(circuit2, repetitions=1000)
        hist = cirq.plot_state_histogram(result, plt.subplot(), title = 'Qubit States', xlabel = 'States', ylabel = 'Occurrences', tick_label=['000', '001', '010', '011', '100', '101', '110', '111'])
        plt.show()


    def plot_density_matrix(self):
        sns.heatmap(np.abs(self.density_matrix), annot=False, cmap="viridis", xticklabels=['000', '001', '010', '011', '100', '101', '110', '111'], yticklabels=['000', '001', '010', '011', '100', '101', '110', '111'])
        plt.title("Density Matrix Absolute Values")
        plt.show()