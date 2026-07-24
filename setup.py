import cirq

class Setup:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = None
        self.circuit = None

    def create_qubits(self):
        #create a list of qubits for the circuit
        self.qubits=cirq.NamedQubit.range(self.num_qubits, prefix = "q")
        pass

    def create_circuit(self):
        #create a GHZ state circuit with the specified number of qubits
        self.circuit=cirq.Circuit()
        self.circuit.append(cirq.H(self.qubits[0]))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        self.circuit.append(cirq.CNOT(self.qubits[1], self.qubits[2]))                    
        pass

    def get_circuit(self):
        #return the created circuit
        return self.circuit
        pass
