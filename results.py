import cirq as cq
import numpy as np
import scipy.linalg #for the matrix operations

class Results:

    #Computes analysis metrics for quantum circuits.  
    
    #Parameters: TBD but will likely taken in a simlulator. 
    #Parameters: vectors will be representated using numpy. 

    def __init__(self):
        self.statevector = None
        self.density_matrix = None
        self.DM_Simulator = cirq.DensityMatrixSimulator()
        self.simulator = cirq.Simulator()

    def simulate_statevector(self, circuit):
        result = self.simulator.simulate(circuit)
        self.statevector = result.final_state_vector
        return self.statevector

        #simulate a circuit and return the statevector

    def simulate_density_matrix(self, circuit):
        toReturn = self.DM_Simulator.simulate(circuit)
        self.density_matrix = toReturn
        return self.density_matrix
        
        #simulate a circuit with noise and return the density matrix

    def density_matrix_from_statevector(self, statevector):
        result = self.density_matrix_from_state_vector(statevector)
        return result
        #Creates a denstiy matrix from a statevector
    
    def fidelity(self, state1, state2):

        sqrt_rho = scipy.linalg.sqrtm(state1)
        fidelity = np.trace(scipy.linalg.sqrtm(sqrt_rho @ state2 @ sqrt_rho)) ** 2
        return fidelity


        #calculate the fidelity between two quantum states
        #return a double

    def von_neumann_entropy(self, density_matrix):
        eigenvalues = np.linalg.eigvalsh(density_matrix)
        eigenvalues = eigenvalues[eigenvalues > 1e-12]  # Filter out small eigenvalues
        entropy = -np.sum(eigenvalues * np.log(eigenvalues))
        return entropy

        #calculate the von neumann entropy of a density matrix
        #return a double

    def partial_trace(self, density_matrix, keep, num_qubits):
        return cirq.partial_trace(density_matrix.reshape([2] * num_qubits * 2), keep_indices=keep).reshape(2 ** len(keep), 2 ** len(keep))
        #reshape that matrices that way they can fit into the cirq.partial_trace function and the final output
        #Compute partial trace of density matrix
        ##### Come back to this later.  

    def is_density_matrix():
        pass
        #determine if a matrix is a valid density matrix

    def purity(self, density_matrix):
        return np.trace(density_matrix @ density_matrix)
        
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
        
