import random
import numpy as np

class Qubit:
    def __init__(self, ID, prob_amplitudes, entangled):
        self.Id = ID
        self.entangled = entangled
        self.prob_amplitudes = prob_amplitudes

def create_qubit(ID, entangled):
    # This function creates a vector representing a qubit
    # The vector is two dimensional and the first number represents the probability amplitude of state 0, seconds number is probability amplitude of state 1
    # The sum of the squares of the amplitudes must equal 1

    amplitude_0 = random.random()
    amplitude_1 = (1-(amplitude_0**2))**0.5
    Id = ID
    return Qubit(Id, np.array([amplitude_0, amplitude_1]), entangled)

def create_entangled_qubits(ID1, ID2, prob_amplitudes, ENTANGLED_ID_COUNT):
    # This function creates two entangled qubits
    # The qubits are represented as a single state vector
    # The state vector is four dimensional and the first number represents the probability amplitude of state 00, second number is probability amplitude of state 01, third number is probability amplitude of state 10, fourth number is probability amplitude of state 11
    # The sum of the squares of the amplitudes must equal 1

    return Qubit(ENTANGLED_ID_COUNT, prob_amplitudes, True)


def measure_qubit(qubit, direction, past_direction):
    # This function meaures a qubit and returns the result of the measurement (0 or 1)

    probability_0 = qubit.prob_amplitudes[0] **2
    probability_1 = qubit.prob_amplitudes[1] **2
    if past_direction is None or np.array_equal(direction, past_direction):
        if random.random() < probability_0:
            qubit.prob_amplitudes = np.array([1, 0])
            return 0
        else:
            qubit.prob_amplitudes = np.array([0, 1])
            return 1
    else:
        qubit.prob_amplitudes = np.array([1/(2**0.5), 1/(2**0.5)])
        if random.random() < 0.5:
            qubit.prob_amplitudes = np.array([1, 0])
            return 0
        else:
            qubit.prob_amplitudes = np.array([0, 1])
            return 1


''' Gates '''

def I(qubit):
    # Equivalent to a wire in a normal circuit
    qubit.prob_amplitudes = np.array([[1, 0], [0, 1]]) @ qubit.prob_amplitudes
    depolarizing_noise(qubit)

def Z(qubit):
    # changes relative phase of the qubit but does not affect basis or probabilities, similar to a wire
    qubit.prob_amplitudes = np.array([[1,0], [0,-1]]) @ qubit.prob_amplitudes
    depolarizing_noise(qubit)

def X(qubit):
    # similar to a NOT gate
    qubit.prob_amplitudes = np.array([[0,1], [1,0]]) @ qubit.prob_amplitudes
    depolarizing_noise(qubit)

def Y(qubit):
    # similar to a NOT gate but with a phase shift
    qubit.prob_amplitudes = np.array([[0,-1], [1,0]]) @ qubit.prob_amplitudes
    depolarizing_noise(qubit)

def H(qubit):
    # puts the qubit into a superposition state
    qubit.prob_amplitudes = np.array([[1/(2**0.5),1/(2**0.5)], [1/(2**0.5),-1/(2**0.5)]]) @ qubit.prob_amplitudes
    depolarizing_noise(qubit)

def CNOT(control_qubit, target_qubit, ENTANGLED_ID_COUNT):
    # flips the target qubit if the control qubit is 1
    # They become entangled and therefore cannot be represented seperately anymore, so we need to represent them as a single state vector
    CNOT_matrix = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])
    state_vector = np.array([control_qubit.prob_amplitudes[0] * target_qubit.prob_amplitudes[0],
                             control_qubit.prob_amplitudes[0] * target_qubit.prob_amplitudes[1],
                             control_qubit.prob_amplitudes[1] * target_qubit.prob_amplitudes[0],
                             control_qubit.prob_amplitudes[1] * target_qubit.prob_amplitudes[1]])
    new_state_vector = CNOT_matrix @ state_vector
    return create_entangled_qubits(control_qubit.Id, target_qubit.Id, new_state_vector, ENTANGLED_ID_COUNT)

def depolarizing_noise(qubit):
    threshold = 0.001
    random_value = random.random()
    if random_value < threshold/3:
        qubit.prob_amplitudes = np.array([[0,1], [1,0]]) @ qubit.prob_amplitudes
    elif threshold/3 <= random_value < 2*threshold/3:
        qubit.prob_amplitudes = np.array([[0,-1], [1,0]]) @ qubit.prob_amplitudes
    elif 2*threshold/3 <= random_value < threshold:
        qubit.prob_amplitudes = np.array([[1,0], [0,-1]]) @ qubit.prob_amplitudes
    else:
        qubit.prob_amplitudes = np.array([[1, 0], [0, 1]]) @ qubit.prob_amplitudes

def main():
    GLOBAL_ID_COUNT = 0
    ENTANGLED_ID_COUNT = 0
    qubit = create_qubit(GLOBAL_ID_COUNT, False)
    print(qubit.prob_amplitudes)
    result = measure_qubit(qubit, np.array([[1,0],[0,1]]), None)
    print(f"Measurement result: {result}")
    result = measure_qubit(qubit, np.array([[1,0],[0,1]]), np.array([[1,0],[0,1]]))
    print(f"Measurement result: {result}")
    result = measure_qubit(qubit, np.array([[1,0],[0,1]]), np.array([[1,0],[0,1]]))
    print(f"Measurement result: {result}")
    GLOBAL_ID_COUNT += 1

if __name__ == "__main__":
    main()