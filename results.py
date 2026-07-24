import cirq as cq
import numpy as np

class Results:

    #Computes analysis metrics for quantum circuits.  
    
    #Parameters: TBD but will likely taken in a simlulator. 
    #Parameters: vectors will be representated using numpy. 

    def __init__(self):
        self.statevector = None
        self.density_matrix = cirq.DensityMatrixSimulator()
        self.simulator = cirq.Simulator()

    def simulate_statevector(self, circuit):
        result = self.simulator.simulate(circuit)
        self.statevector = result.final_state_vector
        return self.statevector

        #simulate a circuit and return the statevector

    def simulate_density_matrix(self, circuit):
        toReturn = self.density_matrix.simulate(circuit)
        self.density_matrix = toReturn
        return self.density_matrix
        pass
        #simulate a circuit with noise and return the density matrix

    def density_matrix_from_statevector(self, statevector):
        result = self.density_matrix_from_state_vector(statevector)
        return result
        pass
        #Creates a denstiy matrix from a statevector

    def fidelity():
        pass
        #calculate the fidelity between two quantum states
        #return a double

    def von_neumann_entropy():
        pass
        #calculate the von neumann entropy of a density matrix
        #return a double

    def partial_trace():
        pass
        #Compute partial trace of density matrix
    

    def is_density_matrix():
        pass
        #determine if a matrix is a valid density matrix

    def purity():
        pass
        #Compute the purity
        #return a double
    def trace_distance():
        pass
        #compute trace distance between two states
        #return a double.
    def average_metric(self, metrics):
        metrics = np.array(metrics)

        return {
            'mean': np.mean(metrics),
            'std': np.std(metrics),
            'min': np.min(metrics),
            'max': np.max(metrics)
        }
        pass
        #compute the average of all metrics
        #this includes fidelity, von neumann entropy, purity, and trace distance
        #also mean, std, min, max etc.   
        
