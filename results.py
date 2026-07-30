import cirq 
import numpy as np
import scipy.linalg #for the matrix operations
from cirq_aqt.aqt_device import AQTNoiseModel
from cirq_aqt.aqt_target_gateset import AQTTargetGateset

class Results:

    #Computes analysis metrics for quantum circuits.  


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
        self.density_matrix = toReturn.final_density_matrix
        return self.density_matrix

        #simulate a circuit with noise and return the density matrix

    def simulate_aqt_density_matrix(self, circuit):
        circuit_no_measure = cirq.Circuit(op for op in circuit.all_operations() if not cirq.is_measurement(op))
        aqt_gateset = AQTTargetGateset()
        compiled_circuit = cirq.optimize_for_target_gateset(circuit_no_measure, gateset=aqt_gateset)
        noise_model = AQTNoiseModel()
        noisy_circuit = compiled_circuit.with_noise(noise_model)
        toReturn = self.DM_Simulator.simulate(noisy_circuit)
        self.density_matrix = toReturn.final_density_matrix
        return self.density_matrix
    
    def density_matrix_from_statevector(self, statevector):
        statevector = np.asarray(statevector, dtype=np.complex128)
        return np.outer(statevector, np.conjugate(statevector))
        #Creates a denstiy matrix from a statevector

    def fidelity(self, state1, state2):

        if state1.ndim == 1:
            state1 = self.density_matrix_from_statevector(state1)
        if state2.ndim == 1:
            state2 = self.density_matrix_from_statevector(state2)
        sqrt_rho = scipy.linalg.sqrtm(state1)
        value = np.trace(scipy.linalg.sqrtm(sqrt_rho @ state2 @ sqrt_rho)) ** 2
        return np.real(value)


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

    def is_density_matrix(self, matrix):
        matrix = np.asarray(matrix)
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            return False
        if not np.allclose(matrix, matrix.conj().T, atol=1e-8):
            #Hermitian check
            return False
        if not np.isclose(np.trace(matrix), 1.0, atol=1e-8):
            #Trace = 1.0 check
            return False
        eigvals = np.linalg.eigvalsh(matrix)
        if np.any(eigvals < -1e-8):
            return False #positive semidefinite check
        return True
        #determine if a matrix is a valid density matrix

    def purity(self, density_matrix):
        return np.trace(density_matrix @ density_matrix)

        #Compute the purity
        #return a double
    def trace_distance(self, state1, state2):
        delta = state1 - state2
        single_values = np.linalg.svd(delta, compute_uv=False)
        return 0.5 * np.sum(single_values)
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
    def qubit_loss_metrics(self):
        return{
            "fidelity": 0.0,
            "density_matrix": "N/A",
            "entropy": "N/A",
            "purity": "N/A",
            "trace_distance": "N/A"
        }
    #this method is specific for neutral atom qubits as the qubits themselves are lost

    def show_results(self, creator, results, circuit, is_trapped_ion):
        if creator.qubit_loss:
            print(results.qubit_loss_metrics)
        else:
            if(is_trapped_ion):
                statevector = results.simulate_statevector(circuit)
                density_matrix = results.simulate_aqt_density_matrix(circuit)
                print("Statevector: ")
                print(statevector)
                print("\n Density Matrix: ")
                print(density_matrix)
                dm_from_sv = results.density_matrix_from_statevector(statevector)
                print("\n Density Matrix from Statevector: ")
                print(dm_from_sv)
            else:
                statevector = results.simulate_statevector(circuit)
                density_matrix = results.simulate_density_matrix(circuit)
                print("Statevector: ")
                print(statevector)
                print("\n Density Matrix: ")
                print(density_matrix)
                dm_from_sv = results.density_matrix_from_statevector(statevector)
                print("\n Density Matrix from Statevector: ")
                print(dm_from_sv)

            #Fidelity
            fid = results.fidelity(dm_from_sv, density_matrix)
            print("\n Fidelity: ")
            print(fid)

            #Von Neumann Entropy
            entropy = results.von_neumann_entropy(density_matrix)
            print("\n Von Neumann Entropy: ")
            print(entropy)

            #Purity
            purity = results.purity(density_matrix)
            print("\n Purity: ")
            print(np.real(purity))

            #Trace Distance
            trace_dist = results.trace_distance(dm_from_sv, density_matrix)
            print("\n Trace Distance: ")
            print(trace_dist)

            #Check if valid density matrix
            valid = results.is_density_matrix(density_matrix)
            print("\n Is Valid Density Matrix: ")
            print(valid)

            #Partial Trace
            num_qubits = len(circuit.all_qubits())

            if num_qubits > 1:
                reduced_dm = results.partial_trace(
                    density_matrix,
                    keep=[0],
                    num_qubits=num_qubits
                )

                print("\nReduced Density Matrix:")
                print(reduced_dm)
