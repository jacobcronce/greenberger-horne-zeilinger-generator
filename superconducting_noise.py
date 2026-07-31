import cirq_google


class Noise:
    
    #applying architecture-specific noise to GHZ state circuits

    def __init__(self, circuit):
        self.circuit = circuit


    #applies noise to a superconducting qubit architecture
    def superconducting_noise(self):
        noise_props = cirq_google.engine.load_device_noise_properties("willow_pink")
        noise_model = cirq_google.NoiseModelFromGoogleNoiseProperties(noise_props)

        return noise_model