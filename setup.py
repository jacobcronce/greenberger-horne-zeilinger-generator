import cirq

class Setup:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = None
        self.circuit = None

    def create_qubits(self):
        #create a list of qubits for the circuit
        pass

    def create_circuit(self):
        #create a GHZ state circuit with the specified number of qubits
        pass

    def get_circuit(self):
        #return the created circuit
        pass