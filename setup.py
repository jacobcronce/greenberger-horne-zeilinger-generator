import cirq
from noise import Noise


class Setup:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubit_loss = False
        self.qubits = None
        self.circuit = None

    def create_qubits(self):
        # create a list of qubits for the circuit
        self.qubits = cirq.NamedQubit.range(self.num_qubits, prefix="q")

    def create_superconducting_circuit(self):
        # create a GHZ state circuit with the specified number of qubits
        self.circuit = cirq.Circuit()
        noise_creator = Noise(self.circuit)
        self.circuit.append(cirq.H(self.qubits[0]))
        noise_creator.superconducting_noise("H", [self.qubits[0]])
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        noise_creator.superconducting_noise("CNOT", [self.qubits[0], self.qubits[1]])
        self.circuit.append(cirq.CNOT(self.qubits[1], self.qubits[2]))
        noise_creator.superconducting_noise("CNOT", [self.qubits[1], self.qubits[2]])
        self.circuit.append(cirq.measure(self.qubits))

    def create_trapped_ion_circuit(self):
        # create a GHZ state circuit with the specified number of qubits
        self.circuit = cirq.Circuit()
        self.circuit.append(cirq.H(self.qubits[0]))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        self.circuit.append(cirq.CNOT(self.qubits[1], self.qubits[2]))
        self.circuit.append(cirq.measure(self.qubits))

    def create_neutral_atom_circuit(self):
        # create a GHZ state circuit with the specified number of qubits
        self.circuit = cirq.Circuit()
        noise_creator = Noise(self.circuit)
        self.circuit.append(cirq.H(self.qubits[0]))
        loss1 = noise_creator.neutral_atom_noise("H", [self.qubits[0]])
        if loss1:
            self.qubit_loss = True
            return 
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        loss2 = noise_creator.neutral_atom_noise(
            "CNOT", [self.qubits[0], self.qubits[1]]
        )
        if loss2:
            return True
        self.circuit.append(cirq.CNOT(self.qubits[1], self.qubits[2]))
        loss3 = noise_creator.neutral_atom_noise(
            "CNOT", [self.qubits[1], self.qubits[2]]
        )
        if loss3:
            return True
        self.circuit.append(cirq.measure(self.qubits))
        return False

    def create_photonic_circuit(self):
        # create a GHZ state circuit with the specified number of qubits
        self.circuit = cirq.Circuit()
        noise_creator = Noise(self.circuit)
        self.circuit.append(cirq.H(self.qubits[0]))
        loss1 = noise_creator.photonic_noise("H", [self.qubits[0]])
        if loss1:
            self.qubit_loss = True
            return 
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        loss2 = noise_creator.photonic_noise("CNOT", [self.qubits[0], self.qubits[1]])
        if loss2:
            return True
        self.circuit.append(cirq.CNOT(self.qubits[1], self.qubits[2]))
        loss3 = noise_creator.photonic_noise("CNOT", [self.qubits[1], self.qubits[2]])
        if loss3:
            return True
        self.circuit.append(cirq.measure(self.qubits))
        return False

    def get_circuit(self):
        # return the created circuit
        return self.circuit
