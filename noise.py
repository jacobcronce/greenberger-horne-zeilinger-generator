import cirq
import numpy as np

class Noise:
    
    #applying architecture-specific noise to GHZ state circuits

    def __init__(self, circuit):
        self.circuit = circuit

    #applies noise to a superconducting qubit architecture
    def superconducting_noise(self, gate, qubits_participated):
        if(gate == 'H'):
            gate_duration = 25e-9
        elif(gate == 'CNOT'):
            gate_duration = 22e-9
        t1_prob = np.exp(-gate_duration/15e-6)
        t2_prob = np.exp(-gate_duration/19e-6)

        #gate depolarization noise
        #self.circuit = self.circuit.with_noise(cirq.depolarize('''probability'''))
        self.circuit.append(cirq)

        #amplitude damping noise (T1 relaxation)
        self.circuit.append(cirq.amplitude_damping(t1_prob).on_each(*qubits_participated))

        #phase damping noise (T2 dephasing)
        self.circuit.append(cirq.phase_damping(t2_prob).on_each(*qubits_participated))

    def trapped_ion_noise(self):
        #applies noise to a trapped ion qubit architecture
        #simulate laser fluctuations and crosstalk between ions
        #circuit object is modified for trapped ion noise
        pass


    def neutral_atom_noise(self):
        #applies noise to a neutral atom qubit architecture
        #simulate rydberg state decay and atom loss
        #circuit object is modified for neutral atom noise
        pass

    def photonic_noise(self):
        #applies noise to a photonic qubit architecture
        #simulate photon loss and mode mismatch
        #amplitude damping for photon loss
        #circuit object is modified for photonic noise
        pass

    def readout_error(self, probability):

        #applies readout error to the circuit
        #simulate measurement errors in the qubits
        #circuit object is modified for readout error
        pass
    
    