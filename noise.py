import cirq
import numpy as np
import random
from cirq import aqt_device

class Noise:
    
    #applying architecture-specific noise to GHZ state circuits

    def __init__(self, circuit):
        self.circuit = circuit

    #applies noise to a superconducting qubit architecture
    def superconducting_noise(self, gate, qubits_participated):
        if(gate == 'H'):
            #obtained from Google research paper
            gate_duration = 25e-9
            #obtained from Willow processor
            depolarizing_probability = 1 - 0.9997
        elif(gate == 'CNOT'):
            #obtained from Google research paper
            gate_duration = 22e-9
            #obtained from Willow processor
            depolarizing_probability = 1 - 0.9988

        #obtained from IBM documentation
        t1_prob = 1 - np.exp(-gate_duration / 15e-6)
        tphi_prob = 1 - np.exp(-gate_duration / (((1/(19e-6))-(1/(30e-6)))**-1))

        #gate depolarization noise
        self.circuit.append(cirq.depolarize(depolarizing_probability).on_each(*qubits_participated))

        #amplitude damping noise (T1 relaxation)
        self.circuit.append(cirq.amplitude_damping(t1_prob).on_each(*qubits_participated))

        #phase damping noise (T2 dephasing)
        self.circuit.append(cirq.phase_damping(tphi_prob).on_each(*qubits_participated))

    def trapped_ion_noise(self):
        #applies noise to a trapped ion qubit architecture
        #will use a simulator for feasibility
        pass


    def neutral_atom_noise(self, gate, qubits_participated, is_first_time):
        #applies noise to a neutral atom qubit architecture
        if(is_first_time):
            #Bluvstein et. al
            if(random.random() <= 0.006):
                return True
            
        
        if(gate == 'H'):
            #Dalal and Sanders
            gate_duration = 1e-6
            depolarizing_probability = 1-0.9997 
        elif(gate == 'CNOT'):
            #Evered et al
            gate_duration = 12e-7
            depolarizing_probability =  1-0.9985
            rydberg_decay_prob = 1 - np.exp(-gate_duration/88e-6)
            self.circuit.append(cirq.amplitude_damping(rydberg_decay_prob).on_each(*qubits_participated))
        
        #Jones et. al
        dephasing_prob = 1 - np.exp(-gate_duration/0.034)

        
        self.circuit.append(cirq.phase_damping(dephasing_prob).on_each(*qubits_participated))
        self.circuit.append(cirq.depolarize(depolarizing_probability).on_each(*qubits_participated))
        return False

        
        
        
    def photonic_noise(self, gate, qubits_participated):
        #applies noise to a photonic qubit architecture
         #Bartolucci et. al
        for qubit in qubits_participated:
            if(random.random() <= 0.027):
                return True
            
        
        if(gate == 'H'):
            depolarizing_probability = 1-0.996
        elif(gate == 'CNOT'):
            depolarizing_probability =  1-0.938
        
        self.circuit.append(cirq.depolarize(depolarizing_probability).on_each(*qubits_participated))
        return False
    
    